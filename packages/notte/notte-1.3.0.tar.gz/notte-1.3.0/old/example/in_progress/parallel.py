import asyncio
from typing import Generic, Protocol, Sequence, TypeVar, runtime_checkable

from typing_extensions import final

# Define types for input and output
Input = TypeVar("Input", covariant=True)
Output = TypeVar("Output", contravariant=True)


# Define protocol for pipes
@runtime_checkable
class PipeProtocol(Protocol[Input, Output]):
    def forward(self, input: Input) -> Output: ...


@runtime_checkable
class AsyncPipeProtocol(Protocol[Input, Output]):
    async def forward(self, input: Input) -> Output: ...


@final
class ParallelPipe(Generic[Input, Output]):
    def __init__(self, pipes: Sequence[PipeProtocol[Input, Output] | AsyncPipeProtocol[Input, Output]]) -> None:
        self.pipes = pipes

    async def forward(self, *inputs: Input) -> list[Output]:
        async def _execute_pipe(
            pipe: PipeProtocol[Input, Output] | AsyncPipeProtocol[Input, Output], input: Input
        ) -> Output:
            if isinstance(pipe, AsyncPipeProtocol):
                return await pipe.forward(input)
            return pipe.forward(input)

        tasks = [_execute_pipe(pipe, input) for pipe, input in zip(self.pipes, inputs)]
        return await asyncio.gather(*tasks)
