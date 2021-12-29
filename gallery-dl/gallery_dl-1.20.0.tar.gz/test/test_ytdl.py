#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2021 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

import os
import sys
import unittest

import re
import shlex

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gallery_dl import ytdl, util, config


class Test_CommandlineArguments(unittest.TestCase):
    module_name = "youtube_dl"

    @classmethod
    def setUpClass(cls):
        try:
            cls.module = __import__(cls.module_name)
        except ImportError:
            raise unittest.SkipTest("cannot import module '{}'".format(
                cls.module_name))
        cls.default = ytdl.parse_command_line(cls.module, [])

    def test_ignore_errors(self):
        self._("--ignore-errors" , "ignoreerrors", True)
        self._("--abort-on-error", "ignoreerrors", False)

    def test_default_search(self):
        self._(["--default-search", "foo"] , "default_search", "foo")

    def test_mark_watched(self):
        self._("--mark-watched"   , "mark_watched", True)
        self._("--no-mark-watched", "mark_watched", False)

    def test_proxy(self):
        self._(["--proxy", "socks5://127.0.0.1:1080/"],
               "proxy", "socks5://127.0.0.1:1080/")
        self._(["--cn-verification-proxy", "https://127.0.0.1"],
               "cn_verification_proxy", "https://127.0.0.1")
        self._(["--geo-verification-proxy", "127.0.0.1"],
               "geo_verification_proxy", "127.0.0.1")

    def test_retries(self):
        inf = float("inf")

        self._(["--retries", "5"], "retries", 5)
        self._(["--retries", "inf"], "retries", inf)
        self._(["--retries", "infinite"], "retries", inf)
        self._(["--fragment-retries", "8"], "fragment_retries", 8)
        self._(["--fragment-retries", "inf"], "fragment_retries", inf)
        self._(["--fragment-retries", "infinite"], "fragment_retries", inf)

    def test_geo_bypass(self):
        self._("--geo-bypass", "geo_bypass", True)
        self._("--no-geo-bypass", "geo_bypass", False)
        self._(["--geo-bypass-country", "EN"], "geo_bypass_country", "EN")
        self._(["--geo-bypass-ip-block", "198.51.100.14/24"],
               "geo_bypass_ip_block", "198.51.100.14/24")

    def test_headers(self):
        headers = self.module.std_headers

        self.assertNotEqual(headers["User-Agent"], "Foo/1.0")
        self._(["--user-agent", "Foo/1.0"])
        self.assertEqual(headers["User-Agent"], "Foo/1.0")

        self.assertNotIn("Referer", headers)
        self._(["--referer", "http://example.org/"])
        self.assertEqual(headers["Referer"], "http://example.org/")

        self.assertNotEqual(headers["Accept"], "*/*")
        self.assertNotIn("DNT", headers)
        self._([
            "--add-header", "accept:*/*",
            "--add-header", "dnt:1",
        ])
        self.assertEqual(headers["accept"], "*/*")
        self.assertEqual(headers["dnt"], "1")

    def test_extract_audio(self):
        opts = self._(["--extract-audio"])
        self.assertEqual(opts["postprocessors"][0], {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "best",
            "preferredquality": "5",
            "nopostoverwrites": False,
        })

        opts = self._([
            "--extract-audio",
            "--audio-format", "opus",
            "--audio-quality", "9",
            "--no-post-overwrites",
        ])
        self.assertEqual(opts["postprocessors"][0], {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "opus",
            "preferredquality": "9",
            "nopostoverwrites": True,
        })

    def test_recode_video(self):
        opts = self._(["--recode-video", " mkv "])
        self.assertEqual(opts["postprocessors"][0], {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mkv",
        })

    def test_subs(self):
        opts = self._(["--convert-subs", "srt"])
        conv = {"key": "FFmpegSubtitlesConvertor", "format": "srt"}
        if self.module_name == "yt_dlp":
            conv["when"] = "before_dl"
        self.assertEqual(opts["postprocessors"][0], conv)

    def test_embed(self):
        subs = {"key": "FFmpegEmbedSubtitle"}
        thumb = {"key": "EmbedThumbnail", "already_have_thumbnail": False}
        if self.module_name == "yt_dlp":
            subs["already_have_subtitle"] = False

        opts = self._(["--embed-subs", "--embed-thumbnail"])
        self.assertEqual(opts["postprocessors"], [subs, thumb])

        thumb["already_have_thumbnail"] = True
        if self.module_name == "yt_dlp":
            subs["already_have_subtitle"] = True

        opts = self._([
            "--embed-thumbnail",
            "--embed-subs",
            "--write-sub",
            "--write-all-thumbnails",
        ])
        self.assertEqual(opts["postprocessors"], [subs, thumb])

    def test_metadata(self):
        opts = self._("--add-metadata")
        self.assertEqual(opts["postprocessors"][0], {"key": "FFmpegMetadata"})

    def test_metadata_from_title(self):
        opts = self._(["--metadata-from-title", "%(artist)s - %(title)s"])
        self.assertEqual(opts["postprocessors"][0], {
            "key": "MetadataFromTitle",
            "titleformat": "%(artist)s - %(title)s",
        })

    def test_xattr(self):
        self._("--xattr-set-filesize", "xattr_set_filesize", True)

        opts = self._("--xattrs")
        self.assertEqual(opts["postprocessors"][0], {"key": "XAttrMetadata"})

    def test_noop(self):
        result = self._([
            "--update",
            "--dump-user-agent",
            "--list-extractors",
            "--extractor-descriptions",
            "--ignore-config",
            "--config-location",
            "--dump-json",
            "--dump-single-json",
            "--list-thumbnails",
        ])

        result["daterange"] = self.default["daterange"]
        self.assertEqual(result, self.default)

    def _(self, cmdline, option=util.SENTINEL, expected=None):
        if isinstance(cmdline, str):
            cmdline = [cmdline]
        result = ytdl.parse_command_line(self.module, cmdline)
        if option is not util.SENTINEL:
            self.assertEqual(result[option], expected, option)
        return result


class Test_CommandlineArguments_YtDlp(Test_CommandlineArguments):
    module_name = "yt_dlp"

    def test_retries_extractor(self):
        inf = float("inf")

        self._(["--extractor-retries", "5"], "extractor_retries", 5)
        self._(["--extractor-retries", "inf"], "extractor_retries", inf)
        self._(["--extractor-retries", "infinite"], "extractor_retries", inf)

    def test_remuxs_video(self):
        opts = self._(["--remux-video", " mkv "])
        self.assertEqual(opts["postprocessors"][0], {
            "key": "FFmpegVideoRemuxer",
            "preferedformat": "mkv",
        })

    def test_metadata(self):
        opts = self._(["--embed-metadata",
                       "--no-embed-chapters",
                       "--embed-info-json"])
        self.assertEqual(opts["postprocessors"][0], {
            "key": "FFmpegMetadata",
            "add_chapters": False,
            "add_metadata": True,
            "add_infojson": True,
        })

    def test_metadata_from_title(self):
        opts = self._(["--metadata-from-title", "%(artist)s - %(title)s"])
        self.assertEqual(opts["postprocessors"][0], {
            "key": "MetadataParser",
            "when": "pre_process",
            "actions": [self.module.MetadataFromFieldPP.to_action(
                "title:%(artist)s - %(title)s")],
        })


if __name__ == "__main__":
    unittest.main(warnings="ignore")

'''
Usage: __main__.py [OPTIONS] URL [URL...]

Options:
  General Options:
    -h, --help                           Print this help text and exit
    --version                            Print program version and exit
    --force-generic-extractor            Force extraction to use the generic
                                         extractor
    --flat-playlist                      Do not extract the videos of a
                                         playlist, only list them.
    --no-color                           Do not emit color codes in output

  Network Options:
    --socket-timeout SECONDS             Time to wait before giving up, in
                                         seconds
    --source-address IP                  Client-side IP address to bind to
    -4, --force-ipv4                     Make all connections via IPv4
    -6, --force-ipv6                     Make all connections via IPv6

  Video Selection:
    --playlist-start NUMBER              Playlist video to start at (default is
                                         1)
    --playlist-end NUMBER                Playlist video to end at (default is
                                         last)
    --playlist-items ITEM_SPEC           Playlist video items to download.
                                         Specify indices of the videos in the
                                         playlist separated by commas like: "--
                                         playlist-items 1,2,5,8" if you want to
                                         download videos indexed 1, 2, 5, 8 in
                                         the playlist. You can specify range: "
                                         --playlist-items 1-3,7,10-13", it will
                                         download the videos at index 1, 2, 3,
                                         7, 10, 11, 12 and 13.
    --match-title REGEX                  Download only matching titles (regex or
                                         caseless sub-string)
    --reject-title REGEX                 Skip download for matching titles
                                         (regex or caseless sub-string)
    --max-downloads NUMBER               Abort after downloading NUMBER files
    --min-filesize SIZE                  Do not download any videos smaller than
                                         SIZE (e.g. 50k or 44.6m)
    --max-filesize SIZE                  Do not download any videos larger than
                                         SIZE (e.g. 50k or 44.6m)
    --date DATE                          Download only videos uploaded in this
                                         date
    --datebefore DATE                    Download only videos uploaded on or
                                         before this date (i.e. inclusive)
    --dateafter DATE                     Download only videos uploaded on or
                                         after this date (i.e. inclusive)
    --min-views COUNT                    Do not download any videos with less
                                         than COUNT views
    --max-views COUNT                    Do not download any videos with more
                                         than COUNT views
    --match-filter FILTER                Generic video filter. Specify any key
                                         (see the "OUTPUT TEMPLATE" for a list
                                         of available keys) to match if the key
                                         is present, !key to check if the key is
                                         not present, key > NUMBER (like
                                         "comment_count > 12", also works with
                                         >=, <, <=, !=, =) to compare against a
                                         number, key = 'LITERAL' (like "uploader
                                         = 'Mike Smith'", also works with !=) to
                                         match against a string literal and & to
                                         require multiple matches. Values which
                                         are not known are excluded unless you
                                         put a question mark (?) after the
                                         operator. For example, to only match
                                         videos that have been liked more than
                                         100 times and disliked less than 50
                                         times (or the dislike functionality is
                                         not available at the given service),
                                         but who also have a description, use
                                         --match-filter "like_count > 100 &
                                         dislike_count <? 50 & description" .
    --no-playlist                        Download only the video, if the URL
                                         refers to a video and a playlist.
    --yes-playlist                       Download the playlist, if the URL
                                         refers to a video and a playlist.
    --age-limit YEARS                    Download only videos suitable for the
                                         given age
    --download-archive FILE              Download only videos not listed in the
                                         archive file. Record the IDs of all
                                         downloaded videos in it.
    --include-ads                        Download advertisements as well
                                         (experimental)

  Download Options:
    -r, --limit-rate RATE                Maximum download rate in bytes per
                                         second (e.g. 50K or 4.2M)
    --skip-unavailable-fragments         Skip unavailable fragments (DASH,
                                         hlsnative and ISM)
    --abort-on-unavailable-fragment      Abort downloading when some fragment is
                                         not available
    --keep-fragments                     Keep downloaded fragments on disk after
                                         downloading is finished; fragments are
                                         erased by default
    --buffer-size SIZE                   Size of download buffer (e.g. 1024 or
                                         16K) (default is 1024)
    --no-resize-buffer                   Do not automatically adjust the buffer
                                         size. By default, the buffer size is
                                         automatically resized from an initial
                                         value of SIZE.
    --http-chunk-size SIZE               Size of a chunk for chunk-based HTTP
                                         downloading (e.g. 10485760 or 10M)
                                         (default is disabled). May be useful
                                         for bypassing bandwidth throttling
                                         imposed by a webserver (experimental)
    --playlist-reverse                   Download playlist videos in reverse
                                         order
    --playlist-random                    Download playlist videos in random
                                         order
    --xattr-set-filesize                 Set file xattribute ytdl.filesize with
                                         expected file size
    --hls-prefer-native                  Use the native HLS downloader instead
                                         of ffmpeg
    --hls-prefer-ffmpeg                  Use ffmpeg instead of the native HLS
                                         downloader
    --hls-use-mpegts                     Use the mpegts container for HLS
                                         videos, allowing to play the video
                                         while downloading (some players may not
                                         be able to play it)
    --external-downloader COMMAND        Use the specified external downloader.
                                         Currently supports aria2c,avconv,axel,c
                                         url,ffmpeg,httpie,wget
    --external-downloader-args ARGS      Give these arguments to the external
                                         downloader

  Filesystem Options:
    -a, --batch-file FILE                File containing URLs to download ('-'
                                         for stdin), one URL per line. Lines
                                         starting with '#', ';' or ']' are
                                         considered as comments and ignored.
    --id                                 Use only video ID in file name
    -o, --output TEMPLATE                Output filename template, see the
                                         "OUTPUT TEMPLATE" for all the info
    --output-na-placeholder PLACEHOLDER  Placeholder value for unavailable meta
                                         fields in output filename template
                                         (default is "NA")
    --autonumber-start NUMBER            Specify the start value for
                                         %(autonumber)s (default is 1)
    --restrict-filenames                 Restrict filenames to only ASCII
                                         characters, and avoid "&" and spaces in
                                         filenames
    -w, --no-overwrites                  Do not overwrite files
    -c, --continue                       Force resume of partially downloaded
                                         files. By default, youtube-dl will
                                         resume downloads if possible.
    --no-continue                        Do not resume partially downloaded
                                         files (restart from beginning)
    --no-part                            Do not use .part files - write directly
                                         into output file
    --no-mtime                           Do not use the Last-modified header to
                                         set the file modification time
    --write-description                  Write video description to a
                                         .description file
    --write-info-json                    Write video metadata to a .info.json
                                         file
    --write-annotations                  Write video annotations to a
                                         .annotations.xml file
    --load-info-json FILE                JSON file containing the video
                                         information (created with the "--write-
                                         info-json" option)
    --cookies FILE                       File to read cookies from and dump
                                         cookie jar in
    --cache-dir DIR                      Location in the filesystem where
                                         youtube-dl can store some downloaded
                                         information permanently. By default
                                         $XDG_CACHE_HOME/youtube-dl or
                                         ~/.cache/youtube-dl . At the moment,
                                         only YouTube player files (for videos
                                         with obfuscated signatures) are cached,
                                         but that may change.
    --no-cache-dir                       Disable filesystem caching
    --rm-cache-dir                       Delete all filesystem cache files

  Thumbnail Options:
    --write-thumbnail                    Write thumbnail image to disk
    --write-all-thumbnails               Write all thumbnail image formats to
                                         disk

  Verbosity / Simulation Options:
    -q, --quiet                          Activate quiet mode
    --no-warnings                        Ignore warnings
    -s, --simulate                       Do not download the video and do not
                                         write anything to disk
    --skip-download                      Do not download the video
    -g, --get-url                        Simulate, quiet but print URL
    -e, --get-title                      Simulate, quiet but print title
    --get-id                             Simulate, quiet but print id
    --get-thumbnail                      Simulate, quiet but print thumbnail URL
    --get-description                    Simulate, quiet but print video
                                         description
    --get-duration                       Simulate, quiet but print video length
    --get-filename                       Simulate, quiet but print output
                                         filename
    --get-format                         Simulate, quiet but print output format
    -j, --dump-json                      Simulate, quiet but print JSON
                                         information. See the "OUTPUT TEMPLATE"
                                         for a description of available keys.
    -J, --dump-single-json               Simulate, quiet but print JSON
                                         information for each command-line
                                         argument. If the URL refers to a
                                         playlist, dump the whole playlist
                                         information in a single line.
    --print-json                         Be quiet and print the video
                                         information as JSON (video is still
                                         being downloaded).
    --newline                            Output progress bar as new lines
    --no-progress                        Do not print progress bar
    --console-title                      Display progress in console titlebar
    -v, --verbose                        Print various debugging information
    --dump-pages                         Print downloaded pages encoded using
                                         base64 to debug problems (very verbose)
    --write-pages                        Write downloaded intermediary pages to
                                         files in the current directory to debug
                                         problems
    --print-traffic                      Display sent and read HTTP traffic
    -C, --call-home                      Contact the youtube-dl server for
                                         debugging
    --no-call-home                       Do NOT contact the youtube-dl server
                                         for debugging

  Workarounds:
    --encoding ENCODING                  Force the specified encoding
                                         (experimental)
    --no-check-certificate               Suppress HTTPS certificate validation
    --prefer-insecure                    Use an unencrypted connection to
                                         retrieve information about the video.
                                         (Currently supported only for YouTube)
    --bidi-workaround                    Work around terminals that lack
                                         bidirectional text support. Requires
                                         bidiv or fribidi executable in PATH
    --sleep-interval SECONDS             Number of seconds to sleep before each
                                         download when used alone or a lower
                                         bound of a range for randomized sleep
                                         before each download (minimum possible
                                         number of seconds to sleep) when used
                                         along with --max-sleep-interval.
    --max-sleep-interval SECONDS         Upper bound of a range for randomized
                                         sleep before each download (maximum
                                         possible number of seconds to sleep).
                                         Must only be used along with --min-
                                         sleep-interval.

  Video Format Options:
    -f, --format FORMAT                  Video format code, see the "FORMAT
                                         SELECTION" for all the info
    --all-formats                        Download all available video formats
    --prefer-free-formats                Prefer free video formats unless a
                                         specific one is requested
    -F, --list-formats                   List all available formats of requested
                                         videos
    --youtube-skip-dash-manifest         Do not download the DASH manifests and
                                         related data on YouTube videos
    --merge-output-format FORMAT         If a merge is required (e.g.
                                         bestvideo+bestaudio), output to given
                                         container format. One of mkv, mp4, ogg,
                                         webm, flv. Ignored if no merge is
                                         required

  Subtitle Options:
    --write-sub                          Write subtitle file
    --write-auto-sub                     Write automatically generated subtitle
                                         file (YouTube only)
    --all-subs                           Download all the available subtitles of
                                         the video
    --list-subs                          List all available subtitles for the
                                         video
    --sub-format FORMAT                  Subtitle format, accepts formats
                                         preference, for example: "srt" or
                                         "ass/srt/best"
    --sub-lang LANGS                     Languages of the subtitles to download
                                         (optional) separated by commas, use
                                         --list-subs for available language tags

  Authentication Options:
    -u, --username USERNAME              Login with this account ID
    -p, --password PASSWORD              Account password. If this option is
                                         left out, youtube-dl will ask
                                         interactively.
    -2, --twofactor TWOFACTOR            Two-factor authentication code
    -n, --netrc                          Use .netrc authentication data
    --video-password PASSWORD            Video password (vimeo, youku)

  Adobe Pass Options:
    --ap-mso MSO                         Adobe Pass multiple-system operator (TV
                                         provider) identifier, use --ap-list-mso
                                         for a list of available MSOs
    --ap-username USERNAME               Multiple-system operator account login
    --ap-password PASSWORD               Multiple-system operator account
                                         password. If this option is left out,
                                         youtube-dl will ask interactively.
    --ap-list-mso                        List all supported multiple-system
                                         operators

  Post-processing Options:
    --postprocessor-args ARGS            Give these arguments to the
                                         postprocessor
    -k, --keep-video                     Keep the video file on disk after the
                                         post-processing; the video is erased by
                                         default
    --prefer-avconv                      Prefer avconv over ffmpeg for running
                                         the postprocessors
    --prefer-ffmpeg                      Prefer ffmpeg over avconv for running
                                         the postprocessors (default)
    --ffmpeg-location PATH               Location of the ffmpeg/avconv binary;
                                         either the path to the binary or its
                                         containing directory.
    --exec CMD                           Execute a command on the file after
                                         downloading and post-processing,
                                         similar to find's -exec syntax.
                                         Example: --exec 'adb push {}
                                         /sdcard/Music/ && rm {}'
    --convert-subs FORMAT                Convert the subtitles to other format
                                         (currently supported: srt|ass|vtt|lrc)

'''
