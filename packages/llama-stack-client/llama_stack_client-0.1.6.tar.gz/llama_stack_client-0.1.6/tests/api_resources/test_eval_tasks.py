# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import Benchmark, BenchmarkListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvalTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        eval_task = client.eval_tasks.retrieve(
            "eval_task_id",
        )
        assert_matches_type(Optional[Benchmark], eval_task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.eval_tasks.with_raw_response.retrieve(
            "eval_task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_task = response.parse()
        assert_matches_type(Optional[Benchmark], eval_task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.eval_tasks.with_streaming_response.retrieve(
            "eval_task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_task = response.parse()
            assert_matches_type(Optional[Benchmark], eval_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_task_id` but received ''"):
            client.eval_tasks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        eval_task = client.eval_tasks.list()
        assert_matches_type(BenchmarkListResponse, eval_task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.eval_tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_task = response.parse()
        assert_matches_type(BenchmarkListResponse, eval_task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.eval_tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_task = response.parse()
            assert_matches_type(BenchmarkListResponse, eval_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        eval_task = client.eval_tasks.register(
            dataset_id="dataset_id",
            eval_task_id="eval_task_id",
            scoring_functions=["string"],
        )
        assert eval_task is None

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        eval_task = client.eval_tasks.register(
            dataset_id="dataset_id",
            eval_task_id="eval_task_id",
            scoring_functions=["string"],
            metadata={"foo": True},
            provider_benchmark_id="provider_benchmark_id",
            provider_id="provider_id",
        )
        assert eval_task is None

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        response = client.eval_tasks.with_raw_response.register(
            dataset_id="dataset_id",
            eval_task_id="eval_task_id",
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_task = response.parse()
        assert eval_task is None

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with client.eval_tasks.with_streaming_response.register(
            dataset_id="dataset_id",
            eval_task_id="eval_task_id",
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_task = response.parse()
            assert eval_task is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEvalTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        eval_task = await async_client.eval_tasks.retrieve(
            "eval_task_id",
        )
        assert_matches_type(Optional[Benchmark], eval_task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval_tasks.with_raw_response.retrieve(
            "eval_task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_task = await response.parse()
        assert_matches_type(Optional[Benchmark], eval_task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval_tasks.with_streaming_response.retrieve(
            "eval_task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_task = await response.parse()
            assert_matches_type(Optional[Benchmark], eval_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `eval_task_id` but received ''"):
            await async_client.eval_tasks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        eval_task = await async_client.eval_tasks.list()
        assert_matches_type(BenchmarkListResponse, eval_task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval_tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_task = await response.parse()
        assert_matches_type(BenchmarkListResponse, eval_task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval_tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_task = await response.parse()
            assert_matches_type(BenchmarkListResponse, eval_task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        eval_task = await async_client.eval_tasks.register(
            dataset_id="dataset_id",
            eval_task_id="eval_task_id",
            scoring_functions=["string"],
        )
        assert eval_task is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        eval_task = await async_client.eval_tasks.register(
            dataset_id="dataset_id",
            eval_task_id="eval_task_id",
            scoring_functions=["string"],
            metadata={"foo": True},
            provider_benchmark_id="provider_benchmark_id",
            provider_id="provider_id",
        )
        assert eval_task is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.eval_tasks.with_raw_response.register(
            dataset_id="dataset_id",
            eval_task_id="eval_task_id",
            scoring_functions=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval_task = await response.parse()
        assert eval_task is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.eval_tasks.with_streaming_response.register(
            dataset_id="dataset_id",
            eval_task_id="eval_task_id",
            scoring_functions=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval_task = await response.parse()
            assert eval_task is None

        assert cast(Any, response.is_closed) is True
