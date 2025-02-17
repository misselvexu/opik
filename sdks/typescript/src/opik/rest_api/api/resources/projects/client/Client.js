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
exports.Projects = void 0;
const environments = __importStar(require("../../../../environments"));
const core = __importStar(require("../../../../core"));
const OpikApi = __importStar(require("../../../index"));
const url_join_1 = __importDefault(require("url-join"));
const serializers = __importStar(require("../../../../serialization/index"));
const errors = __importStar(require("../../../../errors/index"));
/**
 * Project related resources
 */
class Projects {
    constructor(_options = {}) {
        this._options = _options;
    }
    /**
     * Find projects
     *
     * @param {OpikApi.FindProjectsRequest} request
     * @param {Projects.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.projects.findProjects()
     */
    findProjects(request = {}, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const { page, size, name, sorting } = request;
            const _queryParams = {};
            if (page != null) {
                _queryParams["page"] = page.toString();
            }
            if (size != null) {
                _queryParams["size"] = size.toString();
            }
            if (name != null) {
                _queryParams["name"] = name;
            }
            if (sorting != null) {
                _queryParams["sorting"] = sorting;
            }
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/projects"),
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
                    body: serializers.ProjectPagePublic.parseOrThrow(_response.body, {
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
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling GET /v1/private/projects.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Create project
     *
     * @param {OpikApi.ProjectWrite} request
     * @param {Projects.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @throws {@link OpikApi.BadRequestError}
     * @throws {@link OpikApi.UnprocessableEntityError}
     *
     * @example
     *     await client.projects.createProject({
     *         name: "name"
     *     })
     */
    createProject(request, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/projects"),
                method: "POST",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.ProjectWrite.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
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
                switch (_response.error.statusCode) {
                    case 400:
                        throw new OpikApi.BadRequestError(_response.error.body);
                    case 422:
                        throw new OpikApi.UnprocessableEntityError(_response.error.body);
                    default:
                        throw new errors.OpikApiError({
                            statusCode: _response.error.statusCode,
                            body: _response.error.body,
                        });
                }
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling POST /v1/private/projects.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Get project by id
     *
     * @param {string} id
     * @param {Projects.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.projects.getProjectById("id")
     */
    getProjectById(id, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/projects/${encodeURIComponent(id)}`),
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
                    body: serializers.ProjectPublic.parseOrThrow(_response.body, {
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
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling GET /v1/private/projects/{id}.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Delete project by id
     *
     * @param {string} id
     * @param {Projects.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @throws {@link OpikApi.ConflictError}
     *
     * @example
     *     await client.projects.deleteProjectById("id")
     */
    deleteProjectById(id, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/projects/${encodeURIComponent(id)}`),
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
                switch (_response.error.statusCode) {
                    case 409:
                        throw new OpikApi.ConflictError(_response.error.body);
                    default:
                        throw new errors.OpikApiError({
                            statusCode: _response.error.statusCode,
                            body: _response.error.body,
                        });
                }
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling DELETE /v1/private/projects/{id}.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Update project by id
     *
     * @param {string} id
     * @param {OpikApi.ProjectUpdate} request
     * @param {Projects.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @throws {@link OpikApi.BadRequestError}
     * @throws {@link OpikApi.UnprocessableEntityError}
     *
     * @example
     *     await client.projects.updateProject("id")
     */
    updateProject(id, request = {}, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/projects/${encodeURIComponent(id)}`),
                method: "PATCH",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.ProjectUpdate.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
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
                switch (_response.error.statusCode) {
                    case 400:
                        throw new OpikApi.BadRequestError(_response.error.body);
                    case 422:
                        throw new OpikApi.UnprocessableEntityError(_response.error.body);
                    default:
                        throw new errors.OpikApiError({
                            statusCode: _response.error.statusCode,
                            body: _response.error.body,
                        });
                }
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling PATCH /v1/private/projects/{id}.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Gets specified metrics for a project
     *
     * @param {string} id
     * @param {OpikApi.ProjectMetricRequestPublic} request
     * @param {Projects.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @throws {@link OpikApi.BadRequestError}
     * @throws {@link OpikApi.NotFoundError}
     *
     * @example
     *     await client.projects.getProjectMetrics("id")
     */
    getProjectMetrics(id, request = {}, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, `v1/private/projects/${encodeURIComponent(id)}/metrics`),
                method: "POST",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.ProjectMetricRequestPublic.jsonOrThrow(request, {
                    unrecognizedObjectKeys: "strip",
                }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: serializers.ProjectMetricResponsePublic.parseOrThrow(_response.body, {
                        unrecognizedObjectKeys: "passthrough",
                        allowUnrecognizedUnionMembers: true,
                        allowUnrecognizedEnumValues: true,
                        breadcrumbsPrefix: ["response"],
                    }),
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                switch (_response.error.statusCode) {
                    case 400:
                        throw new OpikApi.BadRequestError(_response.error.body);
                    case 404:
                        throw new OpikApi.NotFoundError(_response.error.body);
                    default:
                        throw new errors.OpikApiError({
                            statusCode: _response.error.statusCode,
                            body: _response.error.body,
                        });
                }
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling POST /v1/private/projects/{id}/metrics.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
    /**
     * Retrieve project
     *
     * @param {OpikApi.ProjectRetrievePublic} request
     * @param {Projects.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @throws {@link OpikApi.BadRequestError}
     * @throws {@link OpikApi.NotFoundError}
     * @throws {@link OpikApi.UnprocessableEntityError}
     *
     * @example
     *     await client.projects.retrieveProject({
     *         name: "name"
     *     })
     */
    retrieveProject(request, requestOptions) {
        return core.APIPromise.from((() => __awaiter(this, void 0, void 0, function* () {
            var _a;
            const _response = yield core.fetcher({
                url: (0, url_join_1.default)((_a = (yield core.Supplier.get(this._options.environment))) !== null && _a !== void 0 ? _a : environments.OpikApiEnvironment.Default, "v1/private/projects/retrieve"),
                method: "POST",
                headers: Object.assign({ "X-Fern-Language": "JavaScript", "X-Fern-Runtime": core.RUNTIME.type, "X-Fern-Runtime-Version": core.RUNTIME.version }, requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.headers),
                contentType: "application/json",
                requestType: "json",
                body: serializers.ProjectRetrievePublic.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" }),
                timeoutMs: (requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.timeoutInSeconds) != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.maxRetries,
                abortSignal: requestOptions === null || requestOptions === void 0 ? void 0 : requestOptions.abortSignal,
            });
            if (_response.ok) {
                return {
                    ok: _response.ok,
                    body: serializers.ProjectPublic.parseOrThrow(_response.body, {
                        unrecognizedObjectKeys: "passthrough",
                        allowUnrecognizedUnionMembers: true,
                        allowUnrecognizedEnumValues: true,
                        breadcrumbsPrefix: ["response"],
                    }),
                    headers: _response.headers,
                };
            }
            if (_response.error.reason === "status-code") {
                switch (_response.error.statusCode) {
                    case 400:
                        throw new OpikApi.BadRequestError(_response.error.body);
                    case 404:
                        throw new OpikApi.NotFoundError(_response.error.body);
                    case 422:
                        throw new OpikApi.UnprocessableEntityError(_response.error.body);
                    default:
                        throw new errors.OpikApiError({
                            statusCode: _response.error.statusCode,
                            body: _response.error.body,
                        });
                }
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.OpikApiError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.OpikApiTimeoutError("Timeout exceeded when calling POST /v1/private/projects/retrieve.");
                case "unknown":
                    throw new errors.OpikApiError({
                        message: _response.error.errorMessage,
                    });
            }
        }))());
    }
}
exports.Projects = Projects;
