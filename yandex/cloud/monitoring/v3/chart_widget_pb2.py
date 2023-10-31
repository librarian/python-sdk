# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/monitoring/v3/chart_widget.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud.monitoring.v3 import downsampling_pb2 as yandex_dot_cloud_dot_monitoring_dot_v3_dot_downsampling__pb2
from yandex.cloud.monitoring.v3 import unit_format_pb2 as yandex_dot_cloud_dot_monitoring_dot_v3_dot_unit__format__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/monitoring/v3/chart_widget.proto\x12\x1ayandex.cloud.monitoring.v3\x1a\x1egoogle/protobuf/wrappers.proto\x1a-yandex/cloud/monitoring/v3/downsampling.proto\x1a,yandex/cloud/monitoring/v3/unit_format.proto\"\xe1 \n\x0b\x43hartWidget\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x07queries\x18\x02 \x01(\x0b\x32/.yandex.cloud.monitoring.v3.ChartWidget.Queries\x12]\n\x16visualization_settings\x18\x03 \x01(\x0b\x32=.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings\x12Q\n\x10series_overrides\x18\x04 \x03(\x0b\x32\x37.yandex.cloud.monitoring.v3.ChartWidget.SeriesOverrides\x12X\n\x14name_hiding_settings\x18\x05 \x01(\x0b\x32:.yandex.cloud.monitoring.v3.ChartWidget.NameHidingSettings\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\r\n\x05title\x18\x07 \x01(\t\x12\x16\n\x0e\x64isplay_legend\x18\x08 \x01(\x08\x12\x46\n\x06\x66reeze\x18\t \x01(\x0e\x32\x36.yandex.cloud.monitoring.v3.ChartWidget.FreezeDuration\x1a\xdc\x01\n\x07Queries\x12G\n\x07targets\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.monitoring.v3.ChartWidget.Queries.Target\x12>\n\x0c\x64ownsampling\x18\x02 \x01(\x0b\x32(.yandex.cloud.monitoring.v3.Downsampling\x1aH\n\x06Target\x12\r\n\x05query\x18\x01 \x01(\t\x12\x11\n\ttext_mode\x18\x02 \x01(\x08\x12\x0e\n\x06hidden\x18\x03 \x01(\x08\x12\x0c\n\x04name\x18\x04 \x01(\t\x1a\xbe\x13\n\x15VisualizationSettings\x12]\n\x04type\x18\x01 \x01(\x0e\x32O.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.VisualizationType\x12\x11\n\tnormalize\x18\x02 \x01(\x08\x12^\n\x0binterpolate\x18\x03 \x01(\x0e\x32I.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.Interpolate\x12\x64\n\x0b\x61ggregation\x18\x04 \x01(\x0e\x32O.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.SeriesAggregation\x12p\n\x15\x63olor_scheme_settings\x18\x05 \x01(\x0b\x32Q.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.ColorSchemeSettings\x12g\n\x10heatmap_settings\x18\x06 \x01(\x0b\x32M.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.HeatmapSettings\x12\x63\n\x0eyaxis_settings\x18\x07 \x01(\x0b\x32K.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.YaxisSettings\x12\r\n\x05title\x18\x08 \x01(\t\x12\x13\n\x0bshow_labels\x18\t \x01(\x08\x1a\xac\x04\n\x13\x43olorSchemeSettings\x12{\n\tautomatic\x18\x01 \x01(\x0b\x32\x66.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.ColorSchemeSettings.AutomaticColorSchemeH\x00\x12y\n\x08standard\x18\x02 \x01(\x0b\x32\x65.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.ColorSchemeSettings.StandardColorSchemeH\x00\x12y\n\x08gradient\x18\x03 \x01(\x0b\x32\x65.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.ColorSchemeSettings.GradientColorSchemeH\x00\x1a\x16\n\x14\x41utomaticColorScheme\x1a\x15\n\x13StandardColorScheme\x1ai\n\x13GradientColorScheme\x12\x13\n\x0bgreen_value\x18\x02 \x01(\t\x12\x14\n\x0cyellow_value\x18\x03 \x01(\t\x12\x11\n\tred_value\x18\x04 \x01(\t\x12\x14\n\x0cviolet_value\x18\x05 \x01(\tB\x08\n\x06scheme\x1a\x65\n\x0fHeatmapSettings\x12\x13\n\x0bgreen_value\x18\x02 \x01(\t\x12\x14\n\x0cyellow_value\x18\x03 \x01(\t\x12\x11\n\tred_value\x18\x04 \x01(\t\x12\x14\n\x0cviolet_value\x18\x05 \x01(\t\x1a\xf4\x01\n\x05Yaxis\x12U\n\x04type\x18\x01 \x01(\x0e\x32G.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.YaxisType\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03min\x18\x03 \x01(\t\x12\x0b\n\x03max\x18\x04 \x01(\t\x12;\n\x0bunit_format\x18\x05 \x01(\x0e\x32&.yandex.cloud.monitoring.v3.UnitFormat\x12.\n\tprecision\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x1a\xb6\x01\n\rYaxisSettings\x12Q\n\x04left\x18\x01 \x01(\x0b\x32\x43.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.Yaxis\x12R\n\x05right\x18\x02 \x01(\x0b\x32\x43.yandex.cloud.monitoring.v3.ChartWidget.VisualizationSettings.Yaxis\"\xae\x02\n\x11VisualizationType\x12\"\n\x1eVISUALIZATION_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17VISUALIZATION_TYPE_LINE\x10\x01\x12\x1c\n\x18VISUALIZATION_TYPE_STACK\x10\x02\x12\x1d\n\x19VISUALIZATION_TYPE_COLUMN\x10\x03\x12\x1d\n\x19VISUALIZATION_TYPE_POINTS\x10\x04\x12\x1a\n\x16VISUALIZATION_TYPE_PIE\x10\x05\x12\x1b\n\x17VISUALIZATION_TYPE_BARS\x10\x06\x12#\n\x1fVISUALIZATION_TYPE_DISTRIBUTION\x10\x07\x12\x1e\n\x1aVISUALIZATION_TYPE_HEATMAP\x10\x08\"o\n\x0bInterpolate\x12\x1b\n\x17INTERPOLATE_UNSPECIFIED\x10\x00\x12\x16\n\x12INTERPOLATE_LINEAR\x10\x01\x12\x14\n\x10INTERPOLATE_LEFT\x10\x02\x12\x15\n\x11INTERPOLATE_RIGHT\x10\x03\"Z\n\tYaxisType\x12\x1a\n\x16YAXIS_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11YAXIS_TYPE_LINEAR\x10\x01\x12\x1a\n\x16YAXIS_TYPE_LOGARITHMIC\x10\x02\"\xc4\x01\n\x11SeriesAggregation\x12\"\n\x1eSERIES_AGGREGATION_UNSPECIFIED\x10\x00\x12\x1a\n\x16SERIES_AGGREGATION_AVG\x10\x01\x12\x1a\n\x16SERIES_AGGREGATION_MIN\x10\x02\x12\x1a\n\x16SERIES_AGGREGATION_MAX\x10\x03\x12\x1b\n\x17SERIES_AGGREGATION_LAST\x10\x04\x12\x1a\n\x16SERIES_AGGREGATION_SUM\x10\x05\x1a\x80\x06\n\x0fSeriesOverrides\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x16\n\x0ctarget_index\x18\x02 \x01(\tH\x00\x12`\n\x08settings\x18\x03 \x01(\x0b\x32N.yandex.cloud.monitoring.v3.ChartWidget.SeriesOverrides.SeriesOverrideSettings\x1a\x9a\x02\n\x16SeriesOverrideSettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12]\n\x04type\x18\x03 \x01(\x0e\x32O.yandex.cloud.monitoring.v3.ChartWidget.SeriesOverrides.SeriesVisualizationType\x12\x12\n\nstack_name\x18\x04 \x01(\t\x12\x11\n\tgrow_down\x18\x05 \x01(\x08\x12]\n\x0eyaxis_position\x18\x06 \x01(\x0e\x32\x45.yandex.cloud.monitoring.v3.ChartWidget.SeriesOverrides.YaxisPosition\"b\n\rYaxisPosition\x12\x1e\n\x1aYAXIS_POSITION_UNSPECIFIED\x10\x00\x12\x17\n\x13YAXIS_POSITION_LEFT\x10\x01\x12\x18\n\x14YAXIS_POSITION_RIGHT\x10\x02\"\xd9\x01\n\x17SeriesVisualizationType\x12)\n%SERIES_VISUALIZATION_TYPE_UNSPECIFIED\x10\x00\x12\"\n\x1eSERIES_VISUALIZATION_TYPE_LINE\x10\x01\x12#\n\x1fSERIES_VISUALIZATION_TYPE_STACK\x10\x02\x12$\n SERIES_VISUALIZATION_TYPE_COLUMN\x10\x03\x12$\n SERIES_VISUALIZATION_TYPE_POINTS\x10\x04\x42\x06\n\x04type\x1a\x35\n\x12NameHidingSettings\x12\x10\n\x08positive\x18\x01 \x01(\x08\x12\r\n\x05names\x18\x02 \x03(\t\"\x99\x01\n\x0e\x46reezeDuration\x12\x1f\n\x1b\x46REEZE_DURATION_UNSPECIFIED\x10\x00\x12\x18\n\x14\x46REEZE_DURATION_HOUR\x10\x01\x12\x17\n\x13\x46REEZE_DURATION_DAY\x10\x02\x12\x18\n\x14\x46REEZE_DURATION_WEEK\x10\x03\x12\x19\n\x15\x46REEZE_DURATION_MONTH\x10\x04\x42k\n\x1eyandex.cloud.api.monitoring.v3ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/monitoring/v3;monitoringb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.monitoring.v3.chart_widget_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036yandex.cloud.api.monitoring.v3ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/monitoring/v3;monitoring'
  _globals['_CHARTWIDGET']._serialized_start=203
  _globals['_CHARTWIDGET']._serialized_end=4396
  _globals['_CHARTWIDGET_QUERIES']._serialized_start=697
  _globals['_CHARTWIDGET_QUERIES']._serialized_end=917
  _globals['_CHARTWIDGET_QUERIES_TARGET']._serialized_start=845
  _globals['_CHARTWIDGET_QUERIES_TARGET']._serialized_end=917
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS']._serialized_start=920
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS']._serialized_end=3414
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_COLORSCHEMESETTINGS']._serialized_start=1614
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_COLORSCHEMESETTINGS']._serialized_end=2170
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_COLORSCHEMESETTINGS_AUTOMATICCOLORSCHEME']._serialized_start=2008
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_COLORSCHEMESETTINGS_AUTOMATICCOLORSCHEME']._serialized_end=2030
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_COLORSCHEMESETTINGS_STANDARDCOLORSCHEME']._serialized_start=2032
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_COLORSCHEMESETTINGS_STANDARDCOLORSCHEME']._serialized_end=2053
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_COLORSCHEMESETTINGS_GRADIENTCOLORSCHEME']._serialized_start=2055
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_COLORSCHEMESETTINGS_GRADIENTCOLORSCHEME']._serialized_end=2160
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_HEATMAPSETTINGS']._serialized_start=2172
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_HEATMAPSETTINGS']._serialized_end=2273
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_YAXIS']._serialized_start=2276
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_YAXIS']._serialized_end=2520
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_YAXISSETTINGS']._serialized_start=2523
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_YAXISSETTINGS']._serialized_end=2705
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_VISUALIZATIONTYPE']._serialized_start=2708
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_VISUALIZATIONTYPE']._serialized_end=3010
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_INTERPOLATE']._serialized_start=3012
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_INTERPOLATE']._serialized_end=3123
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_YAXISTYPE']._serialized_start=3125
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_YAXISTYPE']._serialized_end=3215
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_SERIESAGGREGATION']._serialized_start=3218
  _globals['_CHARTWIDGET_VISUALIZATIONSETTINGS_SERIESAGGREGATION']._serialized_end=3414
  _globals['_CHARTWIDGET_SERIESOVERRIDES']._serialized_start=3417
  _globals['_CHARTWIDGET_SERIESOVERRIDES']._serialized_end=4185
  _globals['_CHARTWIDGET_SERIESOVERRIDES_SERIESOVERRIDESETTINGS']._serialized_start=3575
  _globals['_CHARTWIDGET_SERIESOVERRIDES_SERIESOVERRIDESETTINGS']._serialized_end=3857
  _globals['_CHARTWIDGET_SERIESOVERRIDES_YAXISPOSITION']._serialized_start=3859
  _globals['_CHARTWIDGET_SERIESOVERRIDES_YAXISPOSITION']._serialized_end=3957
  _globals['_CHARTWIDGET_SERIESOVERRIDES_SERIESVISUALIZATIONTYPE']._serialized_start=3960
  _globals['_CHARTWIDGET_SERIESOVERRIDES_SERIESVISUALIZATIONTYPE']._serialized_end=4177
  _globals['_CHARTWIDGET_NAMEHIDINGSETTINGS']._serialized_start=4187
  _globals['_CHARTWIDGET_NAMEHIDINGSETTINGS']._serialized_end=4240
  _globals['_CHARTWIDGET_FREEZEDURATION']._serialized_start=4243
  _globals['_CHARTWIDGET_FREEZEDURATION']._serialized_end=4396
# @@protoc_insertion_point(module_scope)
