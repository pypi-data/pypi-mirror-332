from typing import Any

import structlog

from flowgate.helpers.message import Message

from flowgate.handler import Handler
from flowgate.metrics import statsd
from flowgate.utils import get_callable_representation

logger = structlog.get_logger(__name__)


class CommandHandler(Handler):
    """
    Command handler.

    Handles a command by calling the correct function or method in a handler
    class.
    """

    def _can_handle_command(self, message: Message) -> bool:
        """
        Checks if the command is something we can handle.

        Args:
            message: Consumed message from the bus.

        Returns:
            bool: Flag to indicate if we can handle the command.
        """
        command_class = message.value["class"]
        if command_class not in self.handlers:
            logger.debug("Unhandled command", command_class=command_class)
            return False

        return True

    def _handle_command(self, command: Any, handler_inst: Any = None) -> None:
        """
        Get and call the correct command handler.

        The handler can either be a callable or a name of a method in the
        handler instance.

        Args:
            command: Command to be handled.
            handler_inst: Optional handler instance - probably an instance
                of the aggregate root.
        """
        command_class = command._class
        handler = self.handlers[command_class]

        logger.info("Calling command handler", command_class=command_class)
        if handler_inst:
            handler(handler_inst, command)
        else:
            handler(command)

    def handle(self, message: dict) -> None:
        """
        Apply correct handler for the received command.

        Args:
            message: Consumed message from the bus.
        """
        if not self._can_handle_command(message):
            return

        command = self.message_deserializer(message)
        logger.info("Handling command", command_class=command._class)

        command_class = command._class
        handler = self.handlers[command_class]
        handler_name = get_callable_representation(handler)
        with statsd.timed(
            "flowgate.handler.handle",
            tags=[
                "message_type:command",
                f"message_class:{command_class}",
                f"handler:{handler_name}",
            ],
        ):
            self._handle_command(command)
