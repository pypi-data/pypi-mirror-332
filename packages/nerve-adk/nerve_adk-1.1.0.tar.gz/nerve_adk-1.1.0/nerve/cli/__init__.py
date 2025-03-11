import asyncio
import pathlib
import typing as t

import typer
from loguru import logger

import nerve
from nerve.cli.agents import show_agents
from nerve.cli.create import create_agent
from nerve.cli.defaults import (
    DEFAULT_AGENT_PATH,
    DEFAULT_AGENTS_LOAD_PATH,
    DEFAULT_CONVERSATION_STRATEGY,
    DEFAULT_GENERATOR,
    DEFAULT_MAX_COST,
    DEFAULT_MAX_STEPS,
    DEFAULT_TIMEOUT,
)
from nerve.cli.execute import execute_flow
from nerve.cli.replay import replay
from nerve.generation import conversation
from nerve.runtime import logging

cli = typer.Typer(
    no_args_is_help=True,
    pretty_exceptions_enable=False,
    context_settings={"help_option_names": ["-h", "--help"]},
)


@cli.command(
    context_settings={"help_option_names": ["-h", "--help"]},
    help="List the agents available locally in $HOME/.nerve/agents or a custom path.",
)
def agents(
    path: t.Annotated[
        pathlib.Path,
        typer.Argument(help="Path to the agent or workflow to create"),
    ] = DEFAULT_AGENTS_LOAD_PATH,
) -> None:
    print(f"🧠 nerve v{nerve.__version__}")

    asyncio.run(show_agents(path))


@cli.command(
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Guided procedure for creating a new agent.",
)
def create(
    path: t.Annotated[
        pathlib.Path,
        typer.Argument(help="Path to the agent or workflow to create"),
    ] = DEFAULT_AGENT_PATH,
    task: t.Annotated[
        str | None,
        typer.Option("--task", "-t", help="Task to create the agent for"),
    ] = None,
    default: t.Annotated[
        bool,
        typer.Option("--default", "-d", help="Use default values."),
    ] = False,
) -> None:
    print(f"🧠 nerve v{nerve.__version__}")

    asyncio.run(create_agent(path.absolute(), task=task, default=default))


@cli.command(
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Print the version and exit.",
)
def version() -> None:
    import platform
    import sys

    print(f"platform: {platform.system().lower()} ({platform.machine()})")
    print(f"python:   {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"nerve:    {nerve.__version__}")


@cli.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True, "help_option_names": ["-h", "--help"]},
    no_args_is_help=True,
    help="Execute an agent or a workflow.",
)
def run(
    ctx: typer.Context,
    input_path: t.Annotated[
        pathlib.Path,
        typer.Argument(help="Agent or workflow to execute"),
    ],
    generator: t.Annotated[
        str,
        typer.Option("--generator", "-g", help="Generator to use"),
    ] = DEFAULT_GENERATOR,
    conversation_strategy: t.Annotated[
        str,
        typer.Option("--conversation", "-c", help="Conversation strategy to use"),
    ] = DEFAULT_CONVERSATION_STRATEGY,
    interactive: t.Annotated[
        bool,
        typer.Option("--interactive", "-i", help="Interactive mode"),
    ] = False,
    debug: t.Annotated[
        bool,
        typer.Option("--debug", help="Enable debug logging"),
    ] = False,
    quiet: t.Annotated[
        bool,
        typer.Option("--quiet", "-q", help="Quiet mode"),
    ] = False,
    max_steps: t.Annotated[
        int,
        typer.Option("--max-steps", "-s", help="Maximum number of steps"),
    ] = DEFAULT_MAX_STEPS,
    max_cost: t.Annotated[
        float,
        typer.Option(
            "--max-cost", help="If cost information is available, stop when the cost exceeds this value in USD."
        ),
    ] = DEFAULT_MAX_COST,
    timeout: t.Annotated[
        int | None,
        typer.Option("--timeout", "-t", help="Timeout in seconds"),
    ] = DEFAULT_TIMEOUT,
    log_path: t.Annotated[
        pathlib.Path | None,
        typer.Option("--log", help="Log to a file."),
    ] = None,
    trace: t.Annotated[
        pathlib.Path | None,
        typer.Option("--trace", help="Save the final state to a file."),
    ] = None,
) -> None:
    logging.init(log_path, level="DEBUG" if debug else "SUCCESS" if quiet else "INFO")
    logger.info(f"🧠 nerve v{nerve.__version__}")

    asyncio.run(
        execute_flow(
            input_path,
            generator,
            # convert the conversation strategy string to a valid enum
            conversation.strategy_from_string(conversation_strategy),
            ctx.args,
            max_steps,
            max_cost,
            timeout,
            interactive,
            trace,
        )
    )


@cli.command(
    context_settings={"help_option_names": ["-h", "--help"]},
    no_args_is_help=True,
    help="Replay a trace file.",
)
def play(
    trace_path: t.Annotated[
        pathlib.Path,
        typer.Argument(help="Trace file to replay"),
    ] = pathlib.Path("trace.jsonl"),
    fast: t.Annotated[
        bool,
        typer.Option("--fast", "-f", help="Do not sleep between events"),
    ] = False,
) -> None:
    logging.init(level="INFO")
    logger.info(f"🧠 nerve v{nerve.__version__}")

    asyncio.run(replay(trace_path, fast))
