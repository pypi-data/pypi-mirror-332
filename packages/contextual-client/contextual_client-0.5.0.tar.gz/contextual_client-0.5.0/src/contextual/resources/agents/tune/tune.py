# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents import tune_create_params
from ....types.agents.create_tune_response import CreateTuneResponse

__all__ = ["TuneResource", "AsyncTuneResource"]


class TuneResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TuneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return TuneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TuneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return TuneResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        test_dataset_name: Optional[str] | NotGiven = NOT_GIVEN,
        test_file: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        train_dataset_name: Optional[str] | NotGiven = NOT_GIVEN,
        training_file: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateTuneResponse:
        """
        Create a tuning job for the specified `Agent` to specialize it to your specific
        domain or use case.

        This API initiates an asynchronous tuning task. You can provide the required
        data through one of two ways:

        - Provide a `training_file` and an optional `test_file`. If no `test_file` is
          provided, a portion of the `training_file` will be held out as the test set.
          For easy reusability, the `training_file` is automatically saved as a `Tuning`
          `Dataset`, and the `test_file` as an `Evaluation` `Dataset`. You can manage
          them via the `/datasets/tune` and `/datasets/evaluation` endpoints.

        - Provide a `Tuning` `Dataset` and an optional `Evaluation` `Dataset`. You can
          create a `Tuning` `Dataset` and `Evaluation` `Dataset` using the
          `/datasets/tune` and `/datasets/evaluation` endpoints respectively.

        The API returns a tune job `id` which can be used to check on the status of your
        tuning task through the `GET /tune/jobs/{job_id}/metadata` endpoint.

        After the tuning job is complete, the metadata associated with the tune job will
        include evaluation results and a model ID. You can then deploy the tuned model
        to the agent by editing its config with the tuned model ID and the "Edit Agent"
        API (i.e. the `PUT /agents/{agent_id}` API). To deactivate the tuned model, you
        will need to edit the Agent's config again and set the `llm_model_id` field to
        "default". For an end-to-end walkthrough, see the `Tune & Evaluation Guide`.

        Args:
          agent_id: ID of the Agent to list tuning jobs for

          test_dataset_name: Optional. `Dataset` to use for testing model checkpoints, created through the
              `/datasets/evaluate` API.

          test_file: Optional. Local path to the test data file. The test file should follow the same
              format as the training data file.

          train_dataset_name: `Dataset` to use for training, created through the `/datasets/tune` API. Either
              `train_dataset_name` or `training_file` must be provided, but not both.

          training_file: Local path to the training data file.

              The file should be in JSON array format, where each element of the array is a
              JSON object represents a single training example. The four required fields are
              `guideline`, `prompt`, `reference`, and `knowledge`.

              - `knowledge` (`list[str]`): Retrieved knowledge used to generate the reference
                answer. `knowledge` is a list of retrieved text chunks.

              - `reference` (`str`): The gold-standard answer to the prompt.

              - `guideline` (`str`): Guidelines for model output. If you do not have special
                guidelines for the model's output, you can use the `System Prompt` defined in
                your Agent configuration as the `guideline`.

              - `prompt` (`str`): Question for the model to respond to.

              Example:

              ```json
              [
                {
                  "guideline": "The answer should be accurate.",
                  "prompt": "What was last quarter's revenue?",
                  "reference": "According to recent reports, the Q3 revenue was $1.2 million, a 0.1 million increase from Q2.",
                  "knowledge": [
                      "Quarterly report: Q3 revenue was $1.2 million.",
                      "Quarterly report: Q2 revenue was $1.1 million.",
                      ...
                  ],
                },
                ...
              ]
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        body = deepcopy_minimal(
            {
                "test_dataset_name": test_dataset_name,
                "test_file": test_file,
                "train_dataset_name": train_dataset_name,
                "training_file": training_file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["training_file"], ["test_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/agents/{agent_id}/tune",
            body=maybe_transform(body, tune_create_params.TuneCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateTuneResponse,
        )


class AsyncTuneResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTuneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTuneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTuneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ContextualAI/contextual-client-python#with_streaming_response
        """
        return AsyncTuneResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        test_dataset_name: Optional[str] | NotGiven = NOT_GIVEN,
        test_file: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        train_dataset_name: Optional[str] | NotGiven = NOT_GIVEN,
        training_file: Optional[FileTypes] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateTuneResponse:
        """
        Create a tuning job for the specified `Agent` to specialize it to your specific
        domain or use case.

        This API initiates an asynchronous tuning task. You can provide the required
        data through one of two ways:

        - Provide a `training_file` and an optional `test_file`. If no `test_file` is
          provided, a portion of the `training_file` will be held out as the test set.
          For easy reusability, the `training_file` is automatically saved as a `Tuning`
          `Dataset`, and the `test_file` as an `Evaluation` `Dataset`. You can manage
          them via the `/datasets/tune` and `/datasets/evaluation` endpoints.

        - Provide a `Tuning` `Dataset` and an optional `Evaluation` `Dataset`. You can
          create a `Tuning` `Dataset` and `Evaluation` `Dataset` using the
          `/datasets/tune` and `/datasets/evaluation` endpoints respectively.

        The API returns a tune job `id` which can be used to check on the status of your
        tuning task through the `GET /tune/jobs/{job_id}/metadata` endpoint.

        After the tuning job is complete, the metadata associated with the tune job will
        include evaluation results and a model ID. You can then deploy the tuned model
        to the agent by editing its config with the tuned model ID and the "Edit Agent"
        API (i.e. the `PUT /agents/{agent_id}` API). To deactivate the tuned model, you
        will need to edit the Agent's config again and set the `llm_model_id` field to
        "default". For an end-to-end walkthrough, see the `Tune & Evaluation Guide`.

        Args:
          agent_id: ID of the Agent to list tuning jobs for

          test_dataset_name: Optional. `Dataset` to use for testing model checkpoints, created through the
              `/datasets/evaluate` API.

          test_file: Optional. Local path to the test data file. The test file should follow the same
              format as the training data file.

          train_dataset_name: `Dataset` to use for training, created through the `/datasets/tune` API. Either
              `train_dataset_name` or `training_file` must be provided, but not both.

          training_file: Local path to the training data file.

              The file should be in JSON array format, where each element of the array is a
              JSON object represents a single training example. The four required fields are
              `guideline`, `prompt`, `reference`, and `knowledge`.

              - `knowledge` (`list[str]`): Retrieved knowledge used to generate the reference
                answer. `knowledge` is a list of retrieved text chunks.

              - `reference` (`str`): The gold-standard answer to the prompt.

              - `guideline` (`str`): Guidelines for model output. If you do not have special
                guidelines for the model's output, you can use the `System Prompt` defined in
                your Agent configuration as the `guideline`.

              - `prompt` (`str`): Question for the model to respond to.

              Example:

              ```json
              [
                {
                  "guideline": "The answer should be accurate.",
                  "prompt": "What was last quarter's revenue?",
                  "reference": "According to recent reports, the Q3 revenue was $1.2 million, a 0.1 million increase from Q2.",
                  "knowledge": [
                      "Quarterly report: Q3 revenue was $1.2 million.",
                      "Quarterly report: Q2 revenue was $1.1 million.",
                      ...
                  ],
                },
                ...
              ]
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        body = deepcopy_minimal(
            {
                "test_dataset_name": test_dataset_name,
                "test_file": test_file,
                "train_dataset_name": train_dataset_name,
                "training_file": training_file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["training_file"], ["test_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/agents/{agent_id}/tune",
            body=await async_maybe_transform(body, tune_create_params.TuneCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateTuneResponse,
        )


class TuneResourceWithRawResponse:
    def __init__(self, tune: TuneResource) -> None:
        self._tune = tune

        self.create = to_raw_response_wrapper(
            tune.create,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._tune.jobs)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._tune.models)


class AsyncTuneResourceWithRawResponse:
    def __init__(self, tune: AsyncTuneResource) -> None:
        self._tune = tune

        self.create = async_to_raw_response_wrapper(
            tune.create,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._tune.jobs)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._tune.models)


class TuneResourceWithStreamingResponse:
    def __init__(self, tune: TuneResource) -> None:
        self._tune = tune

        self.create = to_streamed_response_wrapper(
            tune.create,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._tune.jobs)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._tune.models)


class AsyncTuneResourceWithStreamingResponse:
    def __init__(self, tune: AsyncTuneResource) -> None:
        self._tune = tune

        self.create = async_to_streamed_response_wrapper(
            tune.create,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._tune.jobs)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._tune.models)
