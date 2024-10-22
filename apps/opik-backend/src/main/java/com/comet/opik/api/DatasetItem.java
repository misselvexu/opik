package com.comet.opik.api;

import com.comet.opik.api.json.DatasetItemDataDeserializer;
import com.comet.opik.api.validate.DatasetItemInputValidation;
import com.comet.opik.api.validate.SourceValidation;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.NotNull;
import lombok.Builder;
import lombok.RequiredArgsConstructor;

import java.time.Instant;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import java.util.Set;
import java.util.UUID;
import java.util.stream.Collectors;

import static java.util.function.Predicate.not;

@Builder(toBuilder = true)
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
@SourceValidation
@DatasetItemInputValidation
public record DatasetItem(
        @JsonView( {
                DatasetItem.View.Public.class, DatasetItem.View.Write.class}) UUID id,
        @JsonView({DatasetItem.View.Public.class,
                DatasetItem.View.Write.class}) @Schema(deprecated = true, description = "to be deprecated soon, please use data field") JsonNode input,
        @JsonView({DatasetItem.View.Public.class,
                DatasetItem.View.Write.class}) @Schema(deprecated = true, description = "to be deprecated soon, please use data field") JsonNode expectedOutput,
        @JsonView({DatasetItem.View.Public.class,
                DatasetItem.View.Write.class}) @Schema(deprecated = true, description = "to be deprecated soon, please use data field") JsonNode metadata,
        @JsonView({DatasetItem.View.Public.class, DatasetItem.View.Write.class}) UUID traceId,
        @JsonView({DatasetItem.View.Public.class, DatasetItem.View.Write.class}) UUID spanId,
        @JsonView({DatasetItem.View.Public.class, DatasetItem.View.Write.class}) @NotNull DatasetItemSource source,

        @JsonDeserialize(using = DatasetItemDataDeserializer.class) @JsonView({DatasetItem.View.Public.class,
                DatasetItem.View.Write.class}) Map<String, Object> data,
        @JsonView({
                DatasetItem.View.Public.class}) @Schema(accessMode = Schema.AccessMode.READ_ONLY) List<ExperimentItem> experimentItems,
        @JsonView({DatasetItem.View.Public.class}) @Schema(accessMode = Schema.AccessMode.READ_ONLY) Instant createdAt,
        @JsonView({
                DatasetItem.View.Public.class}) @Schema(accessMode = Schema.AccessMode.READ_ONLY) Instant lastUpdatedAt,
        @JsonView({DatasetItem.View.Public.class}) @Schema(accessMode = Schema.AccessMode.READ_ONLY) String createdBy,
        @JsonView({
                DatasetItem.View.Public.class}) @Schema(accessMode = Schema.AccessMode.READ_ONLY) String lastUpdatedBy){

    @Builder(toBuilder = true)
    public record DatasetItemPage(
            @JsonView( {
                    DatasetItem.View.Public.class}) List<DatasetItem> content,
            @JsonView({DatasetItem.View.Public.class}) int page,
            @JsonView({DatasetItem.View.Public.class}) int size,
            @JsonView({DatasetItem.View.Public.class}) long total,
            @JsonView({DatasetItem.View.Public.class}) Set<Column> columns) implements Page<DatasetItem>{

        public record Column(String name, Set<ColumnType> types) {

            @RequiredArgsConstructor
            public enum ColumnType {
                STRING("string"),
                NUMBER("number"),
                OBJECT("object"),
                BOOLEAN("boolean"),
                ARRAY("array"),
                NULL("null");

                @JsonValue
                private final String value;
            }
        }
    }

    public static class View {
        public static class Write {
        }

        public static class Public {
        }
    }

    public DatasetItem {
        if (data != null
                && data.values().stream().filter(Objects::nonNull).anyMatch(not(value -> value instanceof JsonNode))) {
            throw new IllegalArgumentException("Data field must be an Map<String, JsonNode>");
        }
    }

    @JsonIgnore
    public Map<String, JsonNode> jsonNodeData() {
        return Optional.ofNullable(data)
                .map(value -> value.entrySet().stream()
                        .collect(Collectors.toMap(Map.Entry::getKey, entry -> (JsonNode) entry.getValue())))
                .orElse(null);
    }
}
