## 1.29.1 - 2025-03-08
### Extractors
#### Additions
- [tenor] add support ([#6075](https://github.com/mikf/gallery-dl/issues/6075))
#### Fixes
- [bunkr] update API endpoint ([#7097](https://github.com/mikf/gallery-dl/issues/7097))
- [erome] fix `AttributeError` for albums without tags ([#7076](https://github.com/mikf/gallery-dl/issues/7076))
- [furaffinity] fix `artist` metadata ([#6582](https://github.com/mikf/gallery-dl/issues/6582) [#7115](https://github.com/mikf/gallery-dl/issues/7115) [#7123](https://github.com/mikf/gallery-dl/issues/7123) [#7130](https://github.com/mikf/gallery-dl/issues/7130))
- [jpgfish] decrypt file URLs ([#7073](https://github.com/mikf/gallery-dl/issues/7073) [#7079](https://github.com/mikf/gallery-dl/issues/7079) [#7109](https://github.com/mikf/gallery-dl/issues/7109))
- [sankaku] fix search tag limit check
- [vsco] fix `video` extractor ([#7113](https://github.com/mikf/gallery-dl/issues/7113))
- [vsco] fix extracting videos from `/gallery` results ([#7113](https://github.com/mikf/gallery-dl/issues/7113))
#### Improvements
- [bunkr] add `endpoint` option ([#7097](https://github.com/mikf/gallery-dl/issues/7097))
- [danbooru:pool] download posts in pool order, add `order-posts` option ([#7091](https://github.com/mikf/gallery-dl/issues/7091))
- [erome:search] recognize all URL query parameters ([#7125](https://github.com/mikf/gallery-dl/issues/7125))
- [reddit] add `selftext` option ([#7111](https://github.com/mikf/gallery-dl/issues/7111))
- [redgifs:search] support `/search?query=...` URLs ([#7118](https://github.com/mikf/gallery-dl/issues/7118))
- [sankaku] increase wait time on 429 errors ([#7129](https://github.com/mikf/gallery-dl/issues/7129))
- [tiktok] improve `tiktok-range` parsing ([#7098](https://github.com/mikf/gallery-dl/issues/7098))
### Downloaders
- [http] detect Cloudflare/DDoS-Guard challenges ([#7066](https://github.com/mikf/gallery-dl/issues/7066) [#7121](https://github.com/mikf/gallery-dl/issues/7121))
- warn about invalid `subcategory` values ([#7103](https://github.com/mikf/gallery-dl/issues/7103) [#7119](https://github.com/mikf/gallery-dl/issues/7119))
