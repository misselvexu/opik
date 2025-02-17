/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";
import { JsonNode } from "./JsonNode";
import { DatasetItemSource } from "./DatasetItemSource";
import { ExperimentItem } from "./ExperimentItem";
export declare const DatasetItem: core.serialization.ObjectSchema<serializers.DatasetItem.Raw, OpikApi.DatasetItem>;
export declare namespace DatasetItem {
    interface Raw {
        id?: string | null;
        input?: JsonNode.Raw | null;
        expected_output?: JsonNode.Raw | null;
        metadata?: JsonNode.Raw | null;
        trace_id?: string | null;
        span_id?: string | null;
        source: DatasetItemSource.Raw;
        data?: JsonNode.Raw | null;
        experiment_items?: ExperimentItem.Raw[] | null;
        created_at?: string | null;
        last_updated_at?: string | null;
        created_by?: string | null;
        last_updated_by?: string | null;
    }
}
