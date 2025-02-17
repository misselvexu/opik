"use strict";
/**
 * This file was auto-generated by Fern from our API Definition.
 */
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Traces = void 0;
const environments = __importStar(require("../../../../environments"));
const core = __importStar(require("../../../../core"));
const serializers = __importStar(require("../../../../serialization/index"));
const url_join_1 = __importDefault(require("url-join"));
const errors = __importStar(require("../../../../errors/index"));
/**
 * Trace related resources
 */
class Traces {
    constructor(_options = {}) {
        this._options = _options;
    }
    /**
     * Add trace feedback score
     *
     * @param {string} id
     * @param {OpikApi.FeedbackScore} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.addTraceFeedbackScore("id", {
     *         name: "name",
     *         value: 1.1,
     *         source: "ui"
     *     })
     */
    addTraceFeedbackScore(id, request, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/traces/${encodeURIComponent(id)}/feedback-scores`),
                method: "PUT",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.FeedbackScore.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: undefined,
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling PUT /v1/private/traces/{id}/feedback-scores.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Get traces by project_name or project_id
     *
     * @param {OpikApi.GetTracesByProjectRequest} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.getTracesByProject()
     */
    getTracesByProject(request = {}, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const { page, size, projectName, projectId, filters, truncate } = request;
            const _queryParams = {};
            if (page != null) {
                _queryParams["page"] = page.toString();
            }
            if (size != null) {
                _queryParams["size"] = size.toString();
            }
            if (projectName != null) {
                _queryParams["project_name"] = projectName;
            }
            if (projectId != null) {
                _queryParams["project_id"] = projectId;
            }
            if (filters != null) {
                _queryParams["filters"] = filters;
            }
            if (truncate != null) {
                _queryParams["truncate"] = truncate.toString();
            }
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/traces"),
                method: "GET",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                queryParameters: _queryParams,
                requestType: "json",
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: serializers.TracePagePublic.parseOrThrow(_response.body, {
                        unrecognizedObjectKeys: "passthrough",
                        allowUnrecognizedUnionMembers: true,
                        allowUnrecognizedEnumValues: true,
                        breadcrumbsPrefix: ["response"],
                    }),
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling GET /v1/private/traces.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Get trace
     *
     * @param {OpikApi.TraceWrite} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.createTrace({
     *         name: "name",
     *         startTime: "2024-01-15T09:30:00Z"
     *     })
     */
    createTrace(request, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/traces"),
                method: "POST",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.TraceWrite.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: undefined,
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling POST /v1/private/traces.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Create traces
     *
     * @param {OpikApi.TraceBatchWrite} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.createTraces({
     *         traces: [{
     *                 name: "name",
     *                 startTime: "2024-01-15T09:30:00Z"
     *             }]
     *     })
     */
    createTraces(request, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/traces/batch"),
                method: "POST",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.TraceBatchWrite.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: undefined,
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling POST /v1/private/traces/batch.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Get trace by id
     *
     * @param {string} id
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.getTraceById("id")
     */
    getTraceById(id, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/traces/${encodeURIComponent(id)}`),
                method: "GET",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: serializers.TracePublic.parseOrThrow(_response.body, {
                        unrecognizedObjectKeys: "passthrough",
                        allowUnrecognizedUnionMembers: true,
                        allowUnrecognizedEnumValues: true,
                        breadcrumbsPrefix: ["response"],
                    }),
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling GET /v1/private/traces/{id}.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Delete trace by id
     *
     * @param {string} id
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.deleteTraceById("id")
     */
    deleteTraceById(id, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/traces/${encodeURIComponent(id)}`),
                method: "DELETE",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: undefined,
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling DELETE /v1/private/traces/{id}.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Update trace by id
     *
     * @param {string} id
     * @param {OpikApi.TraceUpdate} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.updateTrace("id")
     */
    updateTrace(id, request = {}, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/traces/${encodeURIComponent(id)}`),
                method: "PATCH",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.TraceUpdate.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: undefined,
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling PATCH /v1/private/traces/{id}.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Delete trace feedback score
     *
     * @param {string} id
     * @param {OpikApi.DeleteFeedbackScore} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.deleteTraceFeedbackScore("id", {
     *         name: "name"
     *     })
     */
    deleteTraceFeedbackScore(id, request, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/traces/${encodeURIComponent(id)}/feedback-scores/delete`),
                method: "POST",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.DeleteFeedbackScore.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: undefined,
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling POST /v1/private/traces/{id}/feedback-scores/delete.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Delete traces
     *
     * @param {OpikApi.TracesDelete} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.deleteTraces({
     *         ids: ["ids"]
     *     })
     */
    deleteTraces(request, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/traces/delete"),
                method: "POST",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.TracesDelete.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: undefined,
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling POST /v1/private/traces/delete.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Find Feedback Score names
     *
     * @param {OpikApi.FindFeedbackScoreNames2Request} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.findFeedbackScoreNames2()
     */
    findFeedbackScoreNames2(request = {}, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const { projectId } = request;
            const _queryParams = {};
            if (projectId != null) {
                _queryParams["project_id"] = projectId;
            }
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/traces/feedback-scores/names"),
                method: "GET",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                queryParameters: _queryParams,
                requestType: "json",
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: serializers.traces.findFeedbackScoreNames2.Response.parseOrThrow(_response.body, {
                        unrecognizedObjectKeys: "passthrough",
                        allowUnrecognizedUnionMembers: true,
                        allowUnrecognizedEnumValues: true,
                        breadcrumbsPrefix: ["response"],
                    }),
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling GET /v1/private/traces/feedback-scores/names.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Get trace stats
     *
     * @param {OpikApi.GetTraceStatsRequest} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.getTraceStats()
     */
    getTraceStats(request = {}, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const { projectId, projectName, filters } = request;
            const _queryParams = {};
            if (projectId != null) {
                _queryParams["project_id"] = projectId;
            }
            if (projectName != null) {
                _queryParams["project_name"] = projectName;
            }
            if (filters != null) {
                _queryParams["filters"] = filters;
            }
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/traces/stats"),
                method: "GET",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                queryParameters: _queryParams,
                requestType: "json",
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: serializers.ProjectStatsPublic.parseOrThrow(_response.body, {
                        unrecognizedObjectKeys: "passthrough",
                        allowUnrecognizedUnionMembers: true,
                        allowUnrecognizedEnumValues: true,
                        breadcrumbsPrefix: ["response"],
                    }),
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling GET /v1/private/traces/stats.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Batch feedback scoring for traces
     *
     * @param {OpikApi.FeedbackScoreBatch} request
     * @param {Traces.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.traces.scoreBatchOfTraces({
     *         scores: [{
     *                 id: "id",
     *                 name: "name",
     *                 value: 1.1,
     *                 source: "ui"
     *             }]
     *     })
     */
    scoreBatchOfTraces(request, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/traces/feedback-scores"),
                method: "PUT",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.FeedbackScoreBatch.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: undefined,
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                throw new errors.OpikApiError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling PUT /v1/private/traces/feedback-scores.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
}
exports.Traces = Traces;
