import sys
import os
# Add the parent directory of 'target_platforms' to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ctypes import cdll, c_char_p, c_int
path = os.path.dirname(os.path.realpath(__file__))

gophers = cdll.LoadLibrary(path + '/go_module/gophers.so')
# Set restype for functions at module load time
gophers.ReadJSON.restype = c_char_p
gophers.ReadYAML.restype = c_char_p
gophers.Show.restype = c_char_p
gophers.Head.restype = c_char_p
gophers.Tail.restype = c_char_p
gophers.Vertical.restype = c_char_p
gophers.ColumnOp.restype = c_char_p
gophers.ColumnCollectList.restype = c_char_p
gophers.ColumnCollectSet.restype = c_char_p
gophers.ColumnSplit.restype = c_char_p
gophers.DFColumns.restype = c_char_p
gophers.DFCount.restype = c_int
gophers.DFCountDuplicates.restype = c_int
gophers.DFCountDistinct.restype = c_int
gophers.DFCollect.restype = c_char_p
gophers.DisplayBrowserWrapper.restype = c_char_p
gophers.DisplayWrapper.restype = c_char_p
gophers.DisplayToFileWrapper.restype = c_char_p
gophers.DisplayHTMLWrapper.restype = c_char_p
gophers.DisplayChartWrapper.restype = c_char_p
gophers.BarChartWrapper.restype = c_char_p
gophers.ColumnChartWrapper.restype = c_char_p
gophers.StackedBarChartWrapper.restype = c_char_p
gophers.StackedPercentChartWrapper.restype = c_char_p
gophers.GroupByWrapper.restype = c_char_p
gophers.AggWrapper.restype = c_char_p
gophers.SumWrapper.restype = c_char_p
gophers.MaxWrapper.restype = c_char_p
gophers.MinWrapper.restype = c_char_p
gophers.MedianWrapper.restype = c_char_p
gophers.MeanWrapper.restype = c_char_p
gophers.ModeWrapper.restype = c_char_p
gophers.UniqueWrapper.restype = c_char_p
gophers.FirstWrapper.restype = c_char_p
gophers.CreateDashboardWrapper.restype = c_char_p
gophers.OpenDashboardWrapper.restype = c_char_p
gophers.SaveDashboardWrapper.restype = c_char_p
gophers.AddPageWrapper.restype = c_char_p
gophers.AddHTMLWrapper.restype = c_char_p
gophers.AddDataframeWrapper.restype = c_char_p
gophers.AddChartWrapper.restype = c_char_p
gophers.AddHeadingWrapper.restype = c_char_p
gophers.AddTextWrapper.restype = c_char_p
gophers.AddSubTextWrapper.restype = c_char_p
gophers.AddBulletsWrapper.restype = c_char_p
gophers.ToCSVFileWrapper.restype = c_char_p

from .gophers import *