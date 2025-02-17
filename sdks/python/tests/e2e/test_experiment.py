from typing import Dict, Any

import opik

from opik import Prompt, synchronization
from opik.api_objects.dataset import dataset_item
from opik.evaluation import metrics
from . import verifiers
from .conftest import _random_chars


def test_experiment_creation_via_evaluate_function__happyflow(
    opik_client: opik.Opik, dataset_name: str, experiment_name: str
):
    # TODO: this test is not finished, it does not check experiment items content
    dataset = opik_client.create_dataset(dataset_name)

    dataset.insert(
        [
            {
                "input": {"question": "What is the of capital of France?"},
                "expected_model_output": {"output": "Paris"},
            },
            {
                "input": {"question": "What is the of capital of Germany?"},
                "expected_model_output": {"output": "Berlin"},
            },
            {
                "input": {"question": "What is the of capital of Poland?"},
                "expected_model_output": {"output": "Warsaw"},
            },
        ]
    )

    def task(item: Dict[str, Any]):
        if item["input"] == {"question": "What is the of capital of France?"}:
            return {"output": "Paris"}
        if item["input"] == {"question": "What is the of capital of Germany?"}:
            return {"output": "Berlin"}
        if item["input"] == {"question": "What is the of capital of Poland?"}:
            return {"output": "Krakow"}

        raise AssertionError(
            f"Task received dataset item with an unexpected input: {item['input']}"
        )

    prompt = Prompt(
        name=f"test-experiment-prompt-{_random_chars()}",
        prompt=f"test-experiment-prompt-template-{_random_chars()}",
    )

    equals_metric = metrics.Equals()
    evaluation_result = opik.evaluate(
        dataset=dataset,
        task=task,
        scoring_metrics=[equals_metric],
        experiment_name=experiment_name,
        experiment_config={
            "model_name": "gpt-3.5",
        },
        scoring_key_mapping={
            "reference": lambda x: x["expected_model_output"]["output"],
        },
        prompt=prompt,
    )

    opik.flush_tracker()

    verifiers.verify_experiment(
        opik_client=opik_client,
        id=evaluation_result.experiment_id,
        experiment_name=evaluation_result.experiment_name,
        experiment_metadata={"model_name": "gpt-3.5"},
        traces_amount=3,  # one trace per dataset item
        feedback_scores_amount=1,
        prompt=prompt,
    )
    # TODO: check more content of the experiment
    #
    # EXPECTED_DATASET_ITEMS = [
    #     dataset_item.DatasetItem(
    #         input={"question": "What is the of capital of France?"},
    #         expected_model_output={"output": "Paris"},
    #     ),
    #     dataset_item.DatasetItem(
    #         input={"question": "What is the of capital of Germany?"},
    #         expected_model_output={"output": "Berlin"},
    #     ),
    #     dataset_item.DatasetItem(
    #         input={"question": "What is the of capital of Poland?"},
    #         expected_model_output={"output": "Warsaw"},
    #     ),
    # ]


def test_experiment_creation__experiment_config_not_set__None_metadata_sent_to_backend(
    opik_client: opik.Opik, dataset_name: str, experiment_name: str
):
    dataset = opik_client.create_dataset(dataset_name)

    dataset.insert(
        [
            {
                "input": {"question": "What is the of capital of France?"},
                "reference": "Paris",
            },
        ]
    )

    def task(item: dataset_item.DatasetItem):
        if item["input"] == {"question": "What is the of capital of France?"}:
            return {
                "output": "Paris",
            }

        raise AssertionError(
            f"Task received dataset item with an unexpected input: {item['input']}"
        )

    equals_metric = metrics.Equals()
    evaluation_result = opik.evaluate(
        dataset=dataset,
        task=task,
        scoring_metrics=[equals_metric],
        experiment_name=experiment_name,
    )

    opik.flush_tracker()

    verifiers.verify_experiment(
        opik_client=opik_client,
        id=evaluation_result.experiment_id,
        experiment_name=evaluation_result.experiment_name,
        experiment_metadata=None,
        traces_amount=1,  # one trace per dataset item
        feedback_scores_amount=1,
    )


def test_experiment_creation__name_can_be_omitted(
    opik_client: opik.Opik, dataset_name: str, experiment_name: str
):
    """
    We can send "None" as experiment_name and the backend will set it for us
    """
    dataset = opik_client.create_dataset(dataset_name)

    dataset.insert(
        [
            {
                "input": {"question": "What is the of capital of France?"},
                "reference": "Paris",
            },
        ]
    )

    def task(item: dataset_item.DatasetItem):
        if item["input"] == {"question": "What is the of capital of France?"}:
            return {"output": "Paris"}

        raise AssertionError(
            f"Task received dataset item with an unexpected input: {item['input']}"
        )

    equals_metric = metrics.Equals()
    evaluation_result = opik.evaluate(
        dataset=dataset,
        task=task,
        scoring_metrics=[equals_metric],
        experiment_name=None,
    )

    opik.flush_tracker()

    experiment_id = evaluation_result.experiment_id

    if not synchronization.until(
        lambda: (
            opik_client._rest_client.experiments.get_experiment_by_id(experiment_id)
            is not None
        ),
        allow_errors=True,
    ):
        raise AssertionError(f"Failed to get experiment with id {experiment_id}.")

    experiment_content = opik_client._rest_client.experiments.get_experiment_by_id(
        experiment_id
    )

    assert experiment_content.name is not None


def test_experiment_creation__scoring_metrics_not_set(
    opik_client: opik.Opik, dataset_name: str, experiment_name
):
    """
    We can create an experiment without scoring metrics
    """
    dataset = opik_client.create_dataset(dataset_name)

    dataset.insert(
        [
            {
                "input": {"question": "What is the of capital of France?"},
                "expected_model_output": {"output": "Paris"},
            },
        ]
    )

    def task(item: dataset_item.DatasetItem):
        if item["input"] == {"question": "What is the of capital of France?"}:
            return {
                "output": "Paris",
            }

        raise AssertionError(
            f"Task received dataset item with an unexpected input: {item['input']}"
        )

    evaluation_result = opik.evaluate(
        dataset=dataset,
        task=task,
        experiment_name=experiment_name,
    )

    opik.flush_tracker()

    experiment_id = evaluation_result.experiment_id

    if not synchronization.until(
        lambda: (
            opik_client._rest_client.experiments.get_experiment_by_id(experiment_id)
            is not None
        ),
        allow_errors=True,
    ):
        raise AssertionError(f"Failed to get experiment with id {experiment_id}.")

    verifiers.verify_experiment(
        opik_client=opik_client,
        id=evaluation_result.experiment_id,
        experiment_name=evaluation_result.experiment_name,
        experiment_metadata=None,
        traces_amount=1,
        feedback_scores_amount=0,
    )


def test_evaluate_experiment__an_experiment_created_with_evaluate__then_new_scores_are_added_to_existing_experiment_items__amount_of_feedback_scores_increased(
    opik_client: opik.Opik, dataset_name: str, experiment_name: str
):
    dataset = opik_client.create_dataset(dataset_name)

    dataset.insert(
        [
            {
                "input": {"question": "What is the of capital of France?"},
                "expected_model_output": {"output": "Paris"},
            },
        ]
    )

    def task(item: Dict[str, Any]):
        if item["input"] == {"question": "What is the of capital of France?"}:
            return {
                "output": "Paris",
                "reference": item["expected_model_output"]["output"],
            }

        raise AssertionError(
            f"Task received dataset item with an unexpected input: {item['input']}"
        )

    prompt = Prompt(
        name=f"test-experiment-prompt-{_random_chars()}",
        prompt=f"test-experiment-prompt-template-{_random_chars()}",
    )

    # Create the experiment first
    evaluation_result = opik.evaluate(
        dataset=dataset,
        task=task,
        scoring_metrics=[],
        experiment_name=experiment_name,
        experiment_config={
            "model_name": "gpt-3.5",
        },
        prompt=prompt,
    )
    opik.flush_tracker()

    verifiers.verify_experiment(
        opik_client=opik_client,
        id=evaluation_result.experiment_id,
        experiment_name=evaluation_result.experiment_name,
        experiment_metadata={
            "model_name": "gpt-3.5",
        },
        traces_amount=1,
        feedback_scores_amount=0,
        prompt=prompt,
    )

    # Populate the existing experiment with a new feedback score
    evaluation_result = opik.evaluate_experiment(
        experiment_name=experiment_name,
        scoring_metrics=[
            metrics.Equals(name="metric1"),
            metrics.Equals(name="metric2"),
            metrics.Equals(name="metric3"),
        ],
    )
    opik.flush_tracker()

    verifiers.verify_experiment(
        opik_client=opik_client,
        id=evaluation_result.experiment_id,
        experiment_name=evaluation_result.experiment_name,
        experiment_metadata={
            "model_name": "gpt-3.5",
        },
        traces_amount=1,
        feedback_scores_amount=3,
        prompt=prompt,
    )
