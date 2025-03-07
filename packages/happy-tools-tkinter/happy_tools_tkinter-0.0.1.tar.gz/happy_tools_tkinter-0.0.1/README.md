# happy-tools-tkinter
User interface for the happy-tools-core library using tkinter.

## Installation

Via pip:

```
pip install happy_tools_tkinter
```

Directly from Github:

```
pip install git+https://github.com/wairas/happy-tools.git
pip install git+https://github.com/wairas/happy-tools-tkinter.git
```


## User interfaces

### Data Viewer

```
usage: happy-data-viewer [-h] [--base_folder BASE_FOLDER] [--sample SAMPLE]
                         [--region REGION] [-r INT] [-g INT] [-b INT] [-o INT]
                         [--listbox_selectbackground LISTBOX_SELECTBACKGROUND]
                         [--listbox_selectforeground LISTBOX_SELECTFOREGROUND]
                         [--normalization PLUGIN] [--zoom PERCENT]
                         [-V {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Viewer for HAPPy data folder structures.

optional arguments:
  -h, --help            show this help message and exit
  --base_folder BASE_FOLDER
                        Base folder to display (default: None)
  --sample SAMPLE       The sample to load (default: None)
  --region REGION       The region to load (default: None)
  -r INT, --scale_r INT
                        the wave length to use for the red channel (default:
                        None)
  -g INT, --scale_g INT
                        the wave length to use for the green channel (default:
                        None)
  -b INT, --scale_b INT
                        the wave length to use for the blue channel (default:
                        None)
  -o INT, --opacity INT
                        the opacity to use (0-100) (default: None)
  --listbox_selectbackground LISTBOX_SELECTBACKGROUND
                        The background color to use for selected items in
                        listboxes (default: #4a6984)
  --listbox_selectforeground LISTBOX_SELECTFOREGROUND
                        The foreground color to use for selected items in
                        listboxes (default: #ffffff)
  --normalization PLUGIN
                        the normalization plugin and its options to use
                        (default: norm-simple)
  --zoom PERCENT        the initial zoom to use (%) or -1 for automatic fit
                        (default: -1)
  -V {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
```


### ENVI Viewer

```
usage: happy-envi-viewer [-h] [-s SCAN] [-f BLACK_REFERENCE]
                         [-w WHITE_REFERENCE] [-r INT] [-g INT] [-b INT]
                         [--autodetect_channels] [--no_autodetect_channels]
                         [--keep_aspectratio] [--no_keep_aspectratio]
                         [--check_scan_dimensions]
                         [--no_check_scan_dimensions]
                         [--auto_load_annotations]
                         [--no_auto_load_annotations] [--export_to_scan_dir]
                         [--annotation_color HEXCOLOR]
                         [--predefined_labels LIST] [--redis_host HOST]
                         [--redis_port PORT] [--redis_pw PASSWORD]
                         [--redis_in CHANNEL] [--redis_out CHANNEL]
                         [--redis_connect] [--no_redis_connect]
                         [--marker_size INT] [--marker_color HEXCOLOR]
                         [--min_obj_size INT] [--black_ref_locator LOCATOR]
                         [--black_ref_method METHOD]
                         [--white_ref_locator LOCATOR]
                         [--white_ref_method METHOD]
                         [--black_ref_locator_for_white_ref LOCATOR]
                         [--black_ref_method_for_white_ref METHOD]
                         [--preprocessing PIPELINE]
                         [--log_timestamp_format FORMAT] [--zoom PERCENT]
                         [--normalization PLUGIN]
                         [-V {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

ENVI Hyperspectral Image Viewer. Offers contour detection using SAM (Segment-
Anything: https://github.com/waikato-datamining/pytorch/tree/master/segment-
anything)

optional arguments:
  -h, --help            show this help message and exit
  -s SCAN, --scan SCAN  Path to the scan file (ENVI format) (default: None)
  -f BLACK_REFERENCE, --black_reference BLACK_REFERENCE
                        Path to the black reference file (ENVI format)
                        (default: None)
  -w WHITE_REFERENCE, --white_reference WHITE_REFERENCE
                        Path to the white reference file (ENVI format)
                        (default: None)
  -r INT, --scale_r INT
                        the wave length to use for the red channel (default:
                        None)
  -g INT, --scale_g INT
                        the wave length to use for the green channel (default:
                        None)
  -b INT, --scale_b INT
                        the wave length to use for the blue channel (default:
                        None)
  --autodetect_channels
                        whether to determine the channels from the meta-data
                        (overrides the manually specified channels) (default:
                        None)
  --no_autodetect_channels
                        whether to turn off auto-detection of channels from
                        meta-data (default: None)
  --keep_aspectratio    whether to keep the aspect ratio (default: None)
  --no_keep_aspectratio
                        whether to not keep the aspect ratio (default: None)
  --check_scan_dimensions
                        whether to compare the dimensions of subsequently
                        loaded scans and output a warning if they differ
                        (default: None)
  --no_check_scan_dimensions
                        whether to not compare the dimensions of subsequently
                        loaded scans and output a warning if they differ
                        (default: None)
  --auto_load_annotations
                        whether to automatically load any annotations when
                        loading a scan, black or white ref (default: None)
  --no_auto_load_annotations
                        whether to not automatically load any annotations when
                        loading a scan, black or white ref (default: None)
  --export_to_scan_dir  whether to export images to the scan directory rather
                        than the last one used (default: None)
  --annotation_color HEXCOLOR
                        the color to use for the annotations like contours
                        (hex color) (default: None)
  --predefined_labels LIST
                        the comma-separated list of labels to use (default:
                        None)
  --redis_host HOST     The Redis host to connect to (IP or hostname)
                        (default: None)
  --redis_port PORT     The port the Redis server is listening on (default:
                        None)
  --redis_pw PASSWORD   The password to use with the Redis server (default:
                        None)
  --redis_in CHANNEL    The channel that SAM is receiving images on (default:
                        None)
  --redis_out CHANNEL   The channel that SAM is broadcasting the detections on
                        (default: None)
  --redis_connect       whether to immediately connect to the Redis host
                        (default: None)
  --no_redis_connect    whether to not immediately connect to the Redis host
                        (default: None)
  --marker_size INT     The size in pixels for the SAM points (default: None)
  --marker_color HEXCOLOR
                        the color to use for the SAM points (hex color)
                        (default: None)
  --min_obj_size INT    The minimum size that SAM contours need to have (<= 0
                        for no minimum) (default: None)
  --black_ref_locator LOCATOR
                        the reference locator scheme to use for locating black
                        references, eg rl-manual (default: None)
  --black_ref_method METHOD
                        the black reference method to use for applying black
                        references, eg br-same-size (default: None)
  --white_ref_locator LOCATOR
                        the reference locator scheme to use for locating
                        whites references, eg rl-manual (default: None)
  --white_ref_method METHOD
                        the white reference method to use for applying white
                        references, eg wr-same-size (default: None)
  --black_ref_locator_for_white_ref LOCATOR
                        the reference locator scheme to use for locating black
                        references to apply to the white reference scans, eg
                        rl-manual (default: None)
  --black_ref_method_for_white_ref METHOD
                        the black reference method to use for applying the
                        black reference to the white reference scans, eg br-
                        same-size (default: None)
  --preprocessing PIPELINE
                        the preprocessors to apply to the scan (default: None)
  --log_timestamp_format FORMAT
                        the format string for the logging timestamp, see: http
                        s://docs.python.org/3/library/datetime.html#strftime-
                        and-strptime-format-codes (default: [%H:%M:%S.%f])
  --zoom PERCENT        the initial zoom to use (%) or -1 for automatic fit
                        (default: -1)
  --normalization PLUGIN
                        the normalization plugin and its options to use
                        (default: norm-simple)
  -V {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
```

### Raw checker

```
usage: happy-raw-checker [-h] [-d RAW_DIR] [-f {text,text-compact,csv,json}]

Raw data checker interface. For sanity checks of raw capture data.

optional arguments:
  -h, --help            show this help message and exit
  -d RAW_DIR, --raw_dir RAW_DIR
                        The initial directory (default: None)
  -f {text,text-compact,csv,json}, --output_format {text,text-compact,csv,json}
                        The output format to use in the text box. (default:
                        text)
```
