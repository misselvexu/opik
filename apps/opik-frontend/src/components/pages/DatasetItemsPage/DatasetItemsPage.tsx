import React, {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import findIndex from "lodash/findIndex";
import get from "lodash/get";
import difference from "lodash/difference";
import union from "lodash/union";
import uniqBy from "lodash/uniqBy";
import { NumberParam, StringParam, useQueryParam } from "use-query-params";
import useLocalStorageState from "use-local-storage-state";
import { keepPreviousData } from "@tanstack/react-query";

import Loader from "@/components/shared/Loader/Loader";
import DataTable from "@/components/shared/DataTable/DataTable";
import DataTablePagination from "@/components/shared/DataTablePagination/DataTablePagination";
import { useDatasetIdFromURL } from "@/hooks/useDatasetIdFromURL";
import ColumnsButton from "@/components/shared/ColumnsButton/ColumnsButton";
import useDatasetItemsList from "@/api/datasets/useDatasetItemsList";
import useDatasetById from "@/api/datasets/useDatasetById";
import { DatasetItem } from "@/types/datasets";
import {
  COLUMN_TYPE,
  ColumnData,
  DynamicColumn,
  ROW_HEIGHT,
} from "@/types/shared";
import ResizableSidePanel from "@/components/shared/ResizableSidePanel/ResizableSidePanel";
import DatasetItemPanelContent from "@/components/pages/DatasetItemsPage/DatasetItemPanelContent";
import { DatasetItemRowActionsCell } from "@/components/pages/DatasetItemsPage/DatasetItemRowActionsCell";
import DataTableRowHeightSelector from "@/components/shared/DataTableRowHeightSelector/DataTableRowHeightSelector";
import AddEditDatasetItemDialog from "@/components/pages/DatasetItemsPage/AddEditDatasetItemDialog";
import { Button } from "@/components/ui/button";
import { convertColumnDataToColumn } from "@/lib/table";
import { buildDocsUrl } from "@/lib/utils";
import DataTableNoData from "@/components/shared/DataTableNoData/DataTableNoData";
import IdCell from "@/components/shared/DataTableCells/IdCell";
import AutodetectCell from "@/components/shared/DataTableCells/AutodetectCell";
import { formatDate } from "@/lib/date";

const getRowId = (d: DatasetItem) => d.id;

export const DEFAULT_SELECTED_COLUMNS: string[] = ["id", "created_at"];

const SELECTED_COLUMNS_KEY = "dataset-items-selected-columns";
const COLUMNS_WIDTH_KEY = "dataset-items-columns-width";
const COLUMNS_ORDER_KEY = "dataset-items-columns-order";
const DYNAMIC_COLUMNS_KEY = "dataset-items-dynamic-columns";

const DatasetItemsPage = () => {
  const datasetId = useDatasetIdFromURL();

  const [activeRowId = "", setActiveRowId] = useQueryParam("row", StringParam, {
    updateType: "replaceIn",
  });

  const [page = 1, setPage] = useQueryParam("page", NumberParam, {
    updateType: "replaceIn",
  });

  const [size = 10, setSize] = useQueryParam("size", NumberParam, {
    updateType: "replaceIn",
  });

  const [height = ROW_HEIGHT.small, setHeight] = useQueryParam(
    "height",
    StringParam,
    {
      updateType: "replaceIn",
    },
  );

  const resetDialogKeyRef = useRef(0);
  const [openDialog, setOpenDialog] = useState<boolean>(false);

  const { data: dataset } = useDatasetById({
    datasetId,
  });

  const { data, isPending } = useDatasetItemsList(
    {
      datasetId,
      page: page as number,
      size: size as number,
    },
    {
      placeholderData: keepPreviousData,
    },
  );

  const rows: Array<DatasetItem> = useMemo(() => data?.content ?? [], [data]);
  const dynamicColumns = useMemo(() => {
    return uniqBy(data?.columns ?? [], "name").map<DynamicColumn>((c) => ({
      id: `data.${c.name}`,
      label: c.name,
      type: c.type,
    }));
  }, [data]);
  const noDataText = "There are no dataset items yet";

  const [selectedColumns, setSelectedColumns] = useLocalStorageState<string[]>(
    SELECTED_COLUMNS_KEY,
    {
      defaultValue: DEFAULT_SELECTED_COLUMNS,
    },
  );

  const [columnsOrder, setColumnsOrder] = useLocalStorageState<string[]>(
    COLUMNS_ORDER_KEY,
    {
      defaultValue: [],
    },
  );

  const [, setPresentedDynamicColumns] = useLocalStorageState<string[]>(
    DYNAMIC_COLUMNS_KEY,
    {
      defaultValue: [],
    },
  );

  const [columnsWidth, setColumnsWidth] = useLocalStorageState<
    Record<string, number>
  >(COLUMNS_WIDTH_KEY, {
    defaultValue: {},
  });

  useEffect(() => {
    setPresentedDynamicColumns((cols) => {
      const dynamicColumnsIds = dynamicColumns.map((col) => col.id);
      const newDynamicColumns = difference(dynamicColumnsIds, cols);

      if (newDynamicColumns.length > 0) {
        setSelectedColumns((selected) => union(selected, newDynamicColumns));
      }

      return union(dynamicColumnsIds, cols);
    });
  }, [dynamicColumns, setPresentedDynamicColumns, setSelectedColumns]);

  const columnsData = useMemo(() => {
    const retVal: ColumnData<DatasetItem>[] = [
      {
        id: "id",
        label: "Item ID",
        type: COLUMN_TYPE.string,
        cell: IdCell as never,
      },
    ];

    dynamicColumns.forEach(({ label, id }) => {
      retVal.push({
        id,
        label,
        type: COLUMN_TYPE.string,
        accessorFn: (row) => get(row, ["data", label], ""),
        cell: AutodetectCell as never,
      } as ColumnData<DatasetItem>);
    });

    retVal.push({
      id: "created_at",
      label: "Created",
      type: COLUMN_TYPE.time,
      accessorFn: (row) => formatDate(row.created_at),
    });

    retVal.push({
      id: "last_updated_at",
      label: "Last updated",
      type: COLUMN_TYPE.time,
      accessorFn: (row) => formatDate(row.last_updated_at),
    });

    return retVal;
  }, [dynamicColumns]);

  const columns = useMemo(() => {
    const retVal = convertColumnDataToColumn<DatasetItem, DatasetItem>(
      columnsData,
      {
        columnsOrder,
        columnsWidth,
        selectedColumns,
      },
    );

    retVal.push({
      id: "actions",
      enableHiding: false,
      cell: DatasetItemRowActionsCell,
      size: 48,
      enableResizing: false,
    });

    return retVal;
  }, [columnsData, columnsOrder, columnsWidth, selectedColumns]);

  const handleNewDatasetItemClick = useCallback(() => {
    setOpenDialog(true);
    resetDialogKeyRef.current = resetDialogKeyRef.current + 1;
  }, []);

  const handleRowClick = useCallback(
    (row: DatasetItem) => {
      setActiveRowId((state) => (row.id === state ? "" : row.id));
    },
    [setActiveRowId],
  );

  const rowIndex = findIndex(rows, (row) => activeRowId === row.id);

  const hasNext = rowIndex >= 0 ? rowIndex < rows.length - 1 : false;
  const hasPrevious = rowIndex >= 0 ? rowIndex > 0 : false;

  const handleRowChange = useCallback(
    (shift: number) => {
      setActiveRowId(rows[rowIndex + shift]?.id ?? "");
    },
    [rowIndex, rows, setActiveRowId],
  );

  const handleClose = useCallback(() => setActiveRowId(""), [setActiveRowId]);

  const resizeConfig = useMemo(
    () => ({
      enabled: true,
      onColumnResize: setColumnsWidth,
    }),
    [setColumnsWidth],
  );

  if (isPending) {
    return <Loader />;
  }

  return (
    <div className="pt-6">
      <div className="mb-4 flex items-center justify-between">
        <h1 className="comet-title-l truncate break-words">{dataset?.name}</h1>
      </div>
      <div className="mb-4 flex items-center justify-between gap-8">
        <div className="flex items-center gap-2"></div>
        <div className="flex items-center gap-2">
          <DataTableRowHeightSelector
            type={height as ROW_HEIGHT}
            setType={setHeight}
          />
          <ColumnsButton
            columns={columnsData}
            selectedColumns={selectedColumns}
            onSelectionChange={setSelectedColumns}
            order={columnsOrder}
            onOrderChange={setColumnsOrder}
          ></ColumnsButton>
          <Button variant="default" onClick={handleNewDatasetItemClick}>
            Create dataset item
          </Button>
        </div>
      </div>
      <DataTable
        columns={columns}
        data={rows}
        onRowClick={handleRowClick}
        activeRowId={activeRowId ?? ""}
        resizeConfig={resizeConfig}
        getRowId={getRowId}
        rowHeight={height as ROW_HEIGHT}
        noData={
          <DataTableNoData title={noDataText}>
            <Button variant="link">
              <a
                href={buildDocsUrl(
                  "/evaluation/manage_datasets",
                  "#insert-items",
                )}
                target="_blank"
                rel="noreferrer"
              >
                Check our documentation
              </a>
            </Button>
          </DataTableNoData>
        }
      />
      <div className="py-4">
        <DataTablePagination
          page={page as number}
          pageChange={setPage}
          size={size as number}
          sizeChange={setSize}
          total={data?.total ?? 0}
        ></DataTablePagination>
      </div>
      <ResizableSidePanel
        panelId="dataset-items"
        entity="item"
        open={Boolean(activeRowId)}
        hasPreviousRow={hasPrevious}
        hasNextRow={hasNext}
        onClose={handleClose}
        onRowChange={handleRowChange}
      >
        <DatasetItemPanelContent datasetItemId={activeRowId as string} />
      </ResizableSidePanel>

      <AddEditDatasetItemDialog
        key={resetDialogKeyRef.current}
        datasetId={datasetId}
        open={openDialog}
        setOpen={setOpenDialog}
      />
    </div>
  );
};

export default DatasetItemsPage;
