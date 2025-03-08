import pandas as pd
from _expected import (
    DF_COUNT_OVERLAPS_PATH1,
    DF_COUNT_OVERLAPS_PATH2,
    DF_MERGE_PATH,
    DF_NEAREST_PATH1,
    DF_NEAREST_PATH2,
    DF_OVER_PATH1,
    DF_OVER_PATH2,
    PD_DF_COUNT_OVERLAPS,
    PD_DF_MERGE,
    PD_DF_NEAREST,
    PD_DF_OVERLAP,
)

import polars_bio as pb
from polars_bio.polars_bio import FilterOp


class TestOverlapNative:
    result_csv = pb.overlap(
        DF_OVER_PATH1,
        DF_OVER_PATH2,
        cols1=("contig", "pos_start", "pos_end"),
        cols2=("contig", "pos_start", "pos_end"),
        output_type="pandas.DataFrame",
        overlap_filter=FilterOp.Weak,
    )

    def test_overlap_count(self):
        assert len(self.result_csv) == 16

    def test_overlap_schema_rows(self):
        result_csv = self.result_csv.sort_values(
            by=list(self.result_csv.columns)
        ).reset_index(drop=True)
        expected = PD_DF_OVERLAP
        pd.testing.assert_frame_equal(result_csv, expected)


class TestNearestNative:
    result = pb.nearest(
        DF_NEAREST_PATH1,
        DF_NEAREST_PATH2,
        cols1=("contig", "pos_start", "pos_end"),
        cols2=("contig", "pos_start", "pos_end"),
        output_type="pandas.DataFrame",
        overlap_filter=FilterOp.Weak,
    )

    def test_nearest_count(self):
        print(self.result)
        assert len(self.result) == len(PD_DF_NEAREST)

    def test_nearest_schema_rows(self):
        result = self.result.sort_values(by=list(self.result.columns)).reset_index(
            drop=True
        )
        expected = PD_DF_NEAREST
        pd.testing.assert_frame_equal(result, expected)


class TestCountOverlapsNative:
    result = pb.count_overlaps(
        DF_COUNT_OVERLAPS_PATH1,
        DF_COUNT_OVERLAPS_PATH2,
        cols1=("contig", "pos_start", "pos_end"),
        cols2=("contig", "pos_start", "pos_end"),
        output_type="pandas.DataFrame",
        overlap_filter=FilterOp.Weak,
        naive_query=False,
    )

    def test_count_overlaps_count(self):
        print(self.result)
        assert len(self.result) == len(PD_DF_COUNT_OVERLAPS)

    def test_count_overlaps_schema_rows(self):
        result = self.result.sort_values(by=list(self.result.columns)).reset_index(
            drop=True
        )
        expected = PD_DF_COUNT_OVERLAPS
        pd.testing.assert_frame_equal(result, expected)


class TestMergeNative:
    result = pb.merge(
        DF_MERGE_PATH,
        cols=("contig", "pos_start", "pos_end"),
        output_type="pandas.DataFrame",
        overlap_filter=FilterOp.Strict,
    )

    def test_merge_count(self):
        print(self.result)
        assert len(self.result) == len(PD_DF_MERGE)

    def test_merge_schema_rows(self):
        result = self.result.sort_values(by=list(self.result.columns)).reset_index(
            drop=True
        )
        expected = PD_DF_MERGE
        pd.testing.assert_frame_equal(result, expected)
