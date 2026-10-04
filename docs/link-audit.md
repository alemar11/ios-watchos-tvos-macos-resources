# Link audit — 2026-10-04

## Scope and results

The original README contained **1883 resource entries**, **1,863 distinct external URL strings**, and **1,846 distinct GitHub repositories**. The URL inventory included two malformed tutorial links as well as links in descriptions.

- **1803 resource entries retained** after cleanup.
- **44 entries removed**: 43 unavailable GitHub repositories and the former iOS Cookies directory.
- **36 duplicate entries consolidated**, including repositories whose old URLs now resolve to the same project.
- **256 repository addresses redirected** to a different owner or repository name; canonical addresses are now used.
- **173 archived repositories retained** with an `Archived` tag.
- **14 thematic areas and 93 topics**, with alphabetical entries and a regenerated Contents table. **144 entries** were moved to a more specific topic, beyond renaming or merging the old categories.

Availability is a dated observation, not a guarantee of maintenance, buildability or compatibility with current SDKs. No project builds were attempted.

## Final validation

The updated README contains **1,809 distinct linked external URLs**. A fresh run of `python3 validation.py --online` checked all of them: **1,804 passed**, **0 were missing**, and **5 required review** (the two TLS failures, two Medium bot blocks and Dribbble response documented below). All 1,798 distinct GitHub repositories retained in the final catalogue passed.

The URL set was reconciled after the final category and formatting changes. Local validation and all 12 validator tests passed. The README was rendered through GitHub's Markdown API and visually inspected in Safari, including the Contents table and resource formatting.

## Method

All repository addresses were queried through authenticated GitHub GraphQL, including canonical URL, archive status, description and author-supplied topics. Every `NOT_FOUND` result was retried through the REST repository endpoint: 44 old addresses returned `404`, one of which was repaired using the original EFQRCode project's current location. GitHub cannot distinguish a deleted repository from one made private to this account, so the removed entries are described as unavailable.

The six GitHub branch/subdirectory links, three profile links and two gists were checked through their specific REST endpoints. QueryKit now links directly to its repository. External sites were checked with HTTP GET, redirects and content inspection; alternate addresses and indexed first-party pages were used where direct requests were blocked. HTTP 200 alone was not treated as proof that the original resource remained available.

Tags preserve the original annotations and add explicit framework names from descriptions and platform/framework topics supplied by the repository owners. The original macOS-app and SwiftUI sections also provide classification evidence. Legacy television and watch emoji annotations were converted to platform tags where applicable; the misleading watch annotation on the macOS simulator tool OpenSim was removed. Archived status comes directly from GitHub. Tags are not an exhaustive support matrix.

## Recovered and corrected external links

| Old address or source | Retained source | Evidence |
| --- | --- | --- |
| `EyreFree/EFQRCode` | [EFQRCode](https://github.com/EFPrefix/EFQRCode) | Original project in the EFPrefix organization; repository metadata and README available. |
| Cocoacontrols `vkcheckbox` | [VKCheckbox](https://github.com/vladislav-k/VKCheckbox) | Matching original project and description; old site redirects through JavaScript to `/lander`. |
| Cocoacontrols `asmaplauncher` | [ASMapLauncher](https://github.com/abdullahselek/ASMapLauncher) | Matching original project and description; old site redirects through JavaScript to `/lander`. |
| Cocoacontrols `jmcrainbow` | [JMCRainbow](https://github.com/gulfcoastdev/JMCRainbow) | Matching original project and description; old site redirects through JavaScript to `/lander`. |
| `gaetanzanella.github.io//2018/replicate-apple-maps-overlay/` | [Replicating Apple Maps overlay](https://gaetanzanella.github.io/2018-12-17/replicating-apple-maps-overlay) | Original URL returns 404; author's home page links to the current article, which returns 200. |
| Medium `@philipp307/draw-a-custom-ios-tabbar-shape-27d298a7f4fa` | [How to Draw a Custom TabBar Shape in iOS](https://medium.com/better-programming/draw-a-custom-ios-tabbar-shape-27d298a7f4fa) | Same article and author at the current publication URL. |
| QueryKit profile | [QueryKit repository](https://github.com/QueryKit/QueryKit) | Repository metadata matches the catalogue description. |

## Checks requiring manual interpretation

These sources were retained. A future automated run can still report them as `review`.

| Source | Direct check | Additional evidence and decision |
| --- | --- | --- |
| [IBDesignable tutorial](https://www.thinkandbuild.it/building-custom-ui-element-with-ibdesignable/) | TLS hostname mismatch | Article content remains indexed on the author's site. Updated to HTTPS, retained, current TLS availability unresolved. |
| [Periscope pull-to-refresh tutorial](https://www.thinkandbuild.it/implementing-the-periscope-app-pull-to-refresh/) | TLS hostname mismatch | Article content remains indexed on the author's site. Updated to HTTPS, retained, current TLS availability unresolved. |
| [Custom TabBar tutorial](https://medium.com/better-programming/draw-a-custom-ios-tabbar-shape-27d298a7f4fa) | Original URL blocked with Cloudflare HTTP 403 | Current publication page and article content retrieved via web lookup. |
| [Advanced view-controller transitions tutorial](https://medium.com/flawless-app-stories/cool-custom-view-controller-transitions-advanced-df2d0ca08029) | Cloudflare HTTP 403 | First-party article content available through web search; retained and malformed Markdown repaired. |
| [Replace animation](https://dribbble.com/shots/2067564-Replace) | HTTP 202 with empty body | First-party page retrieved via web lookup with the correct title and creator. |

The SwiftyOS collection-view tutorial returned HTTP 200 with the expected article content. Both gists remain accessible. No resources were removed solely because of archive status, a bot block or a TLS error.

## Removed resources

For GitHub entries below, both GraphQL `NOT_FOUND` and REST HTTP `404` were observed. Their URLs are recorded as text so they remain auditable without presenting them as recommendations.

| Resource | Previous URL | Reason |
| --- | --- | --- |
| ALBNoSQLDB | `https://github.com/AaronBratcher/ALBNoSQLDB` | GitHub GraphQL NOT_FOUND and REST 404 |
| AppleNews-CollectionView | `https://github.com/mhlangagc/AppleNews-CollectionView` | GitHub GraphQL NOT_FOUND and REST 404 |
| ApplozicSwift | `https://github.com/AppLozic/ApplozicSwift` | GitHub GraphQL NOT_FOUND and REST 404 |
| AvatarView | `https://github.com/chrene/AvatarView/` | GitHub GraphQL NOT_FOUND and REST 404 |
| Awesome Mobile Machine Learning | `https://github.com/fritzlabs/Awesome-Mobile-Machine-Learning` | GitHub GraphQL NOT_FOUND and REST 404 |
| Beam for Reddit | `https://github.com/PowerMobileTeam/NewsApp` | GitHub GraphQL NOT_FOUND and REST 404 |
| BNR CoreDataStack | `https://github.com/bignerdranch/CoreDataStack` | GitHub GraphQL NOT_FOUND and REST 404 |
| CircleLoading | `https://github.com/goldmoment/CircleLoading` | GitHub GraphQL NOT_FOUND and REST 404 |
| CleanroomASL | `https://github.com/emaloney/CleanroomASL` | GitHub GraphQL NOT_FOUND and REST 404 |
| CollectionViewSegmentedControl | `https://github.com/JamesSedlacek/CollectionViewSegmentedControl` | GitHub GraphQL NOT_FOUND and REST 404 |
| DRDoubleTapButton | `https://github.com/dgrueda/DRDoubleTapButton` | GitHub GraphQL NOT_FOUND and REST 404 |
| DSGradientProgressView | `https://github.com/DholStudio/DSGradientProgressView` | GitHub GraphQL NOT_FOUND and REST 404 |
| Ello | `https://github.com/ello/ello-ios` | GitHub GraphQL NOT_FOUND and REST 404 |
| Example iOS Apps | `https://github.com/hideiwai/test2` | GitHub GraphQL NOT_FOUND and REST 404 |
| ExpandingViewTransition | `https://github.com/tomkowz/ExpandingViewTransition-Demo` | GitHub GraphQL NOT_FOUND and REST 404 |
| FluidValidator | `https://github.com/frograin/FluidValidator` | GitHub GraphQL NOT_FOUND and REST 404 |
| Freddy | `https://github.com/bignerdranch/Freddy` | GitHub GraphQL NOT_FOUND and REST 404 |
| Graphs | `https://github.com/recruit-mtl/Graphs` | GitHub GraphQL NOT_FOUND and REST 404 |
| GrouponHeader | `https://github.com/JamesSedlacek/GrouponHeader` | GitHub GraphQL NOT_FOUND and REST 404 |
| HighstreetWatchApp | `https://github.com/GetHighstreet/HighstreetWatchApp` | GitHub GraphQL NOT_FOUND and REST 404 |
| ImagePickerCropView_App | `https://github.com/Murad9288/ImagePickerCropView_App` | GitHub GraphQL NOT_FOUND and REST 404 |
| InfiniteScrollListSwiftUI | `https://github.com/itsMeSib/InfiniteScrollListSwiftUI` | GitHub GraphQL NOT_FOUND and REST 404 |
| IntroScreen | `https://github.com/P1xelfehler/IntroScreen` | GitHub GraphQL NOT_FOUND and REST 404 |
| iOS Cookies: A hand curated collection of iOS libraries written in Swift | `http://www.ioscookies.com` | Source replaced by an unrelated cryptocurrency site |
| mChat | `https://github.com/realpaliy/mChat` | GitHub GraphQL NOT_FOUND and REST 404 |
| Messenger | `https://github.com/vitaliy-paliy/Messenger` | GitHub GraphQL NOT_FOUND and REST 404 |
| NaughtyKeyboard | `https://github.com/Palleas/NaughtyKeyboard` | GitHub GraphQL NOT_FOUND and REST 404 |
| NewsApp | `https://github.com/PowerMobileWeb/NewsApp` | GitHub GraphQL NOT_FOUND and REST 404 |
| pet-therapy | `https://github.com/curzel-it/pet-therapy` | GitHub GraphQL NOT_FOUND and REST 404 |
| PopUp | `https://github.com/mhlangagc/PopUp` | GitHub GraphQL NOT_FOUND and REST 404 |
| RichTextView | `https://github.com/tophat/RichTextView` | GitHub GraphQL NOT_FOUND and REST 404 |
| Routing | `https://github.com/jwalapr/Routing` | GitHub GraphQL NOT_FOUND and REST 404 |
| RYFloatingInput | `https://github.com/ChengRayYu/RYFloatingInput` | GitHub GraphQL NOT_FOUND and REST 404 |
| SelectPickerCell | `https://github.com/oclef/SelectPickerCell` | GitHub GraphQL NOT_FOUND and REST 404 |
| Send-App-Usage-Permissio | `https://github.com/snake302/Send-App-Usage-Permission` | GitHub GraphQL NOT_FOUND and REST 404 |
| sismicapp-ios | `https://github.com/jbeleno/sismicapp-ios` | GitHub GraphQL NOT_FOUND and REST 404 |
| SoundCloudSwift | `https://github.com/pepibumur/SoundCloudSwift` | GitHub GraphQL NOT_FOUND and REST 404 |
| sscalendar | `https://github.com/StevenPreston/sscalendar` | GitHub GraphQL NOT_FOUND and REST 404 |
| Swift-CellAnimation | `https://github.com/Mononster/Swift-CellAnimation` | GitHub GraphQL NOT_FOUND and REST 404 |
| SwiftyRegex | `https://github.com/maxadamski/SwiftyRegex` | GitHub GraphQL NOT_FOUND and REST 404 |
| TodayMind | `https://github.com/cyanzhong/TodayMind` | GitHub GraphQL NOT_FOUND and REST 404 |
| UICollectionViewSlideLeft | `https://github.com/antbelldev/UICollectionViewSlideLeft` | GitHub GraphQL NOT_FOUND and REST 404 |
| Wallet | `https://github.com/rshevchuk/Wallet` | GitHub GraphQL NOT_FOUND and REST 404 |
| ZMSwiftRangeSlider | `https://github.com/nanjingboy/ZMSwiftRangeSlider` | GitHub GraphQL NOT_FOUND and REST 404 |

## Repository transfers and renames

Case-only normalization, HTTP-to-HTTPS changes and trailing slash cleanup are omitted from this table.

| Previous repository | Canonical repository |
| --- | --- |
| `10011-studio/floatingtabbar` | [claudiaeng/FloatingTabBar](https://github.com/claudiaeng/FloatingTabBar) |
| `10011-studio/urbanvillageprojectscreens` | [claudiaeng/UrbanVillageProjectScreens](https://github.com/claudiaeng/UrbanVillageProjectScreens) |
| `1024jp/nsdata-gzip` | [1024jp/GzipSwift](https://github.com/1024jp/GzipSwift) |
| `631106979/wclshinebutton` | [imwcl/WCLShineButton](https://github.com/imwcl/WCLShineButton) |
| `abhiperry/addatepicker` | [abhi-dave/ADDatePicker](https://github.com/abhi-dave/ADDatePicker) |
| `aciidb0mb3r/swiflytics` | [aciidgh/Swiflytics](https://github.com/aciidgh/Swiflytics) |
| `alexey-kubas-appus/notification-alertview` | [appus-studio/Notification-AlertView](https://github.com/appus-studio/Notification-AlertView) |
| `alisoftware/swiftgen` | [SwiftGen/SwiftGen](https://github.com/SwiftGen/SwiftGen) |
| `altayer-digital/atgmediabrowser` | [ounass-tech/ATGMediaBrowser](https://github.com/ounass-tech/ATGMediaBrowser) |
| `alwaysrightinstitute/shell` | [helje5/Shell](https://github.com/helje5/Shell) |
| `applidium/adnavigationbarextension` | [faberNovel/ADNavigationBarExtension](https://github.com/faberNovel/ADNavigationBarExtension) |
| `applidium/adoverlaycontainer` | [gaetanzanella/OverlayContainer](https://github.com/gaetanzanella/OverlayContainer) |
| `applidium/overlaycontainer` | [gaetanzanella/OverlayContainer](https://github.com/gaetanzanella/OverlayContainer) |
| `arikis/overdrive` | [saidsikira/Overdrive](https://github.com/saidsikira/Overdrive) |
| `athiercelin/localizations` | [e7711bbear/Localizations](https://github.com/e7711bbear/Localizations) |
| `avavaas/iosluckywheel` | [AhmedNasserSh/iOSLuckyWheel](https://github.com/AhmedNasserSh/iOSLuckyWheel) |
| `babylonpartners/drawerkit` | [babylonhealth/DrawerKit](https://github.com/babylonhealth/DrawerKit) |
| `babyshung/splashwindow` | [RnBlue8/SplashWindow](https://github.com/RnBlue8/SplashWindow) |
| `bakkenbaeck/sectionscrubber` | [3lvis/SectionScrubber](https://github.com/3lvis/SectionScrubber) |
| `bakkenbaeck/viewer` | [3lvis/Viewer](https://github.com/3lvis/Viewer) |
| `beaunouvelle/aspectfillfaceaware` | [BeauNouvelle/FaceAware](https://github.com/BeauNouvelle/FaceAware) |
| `bermudalocket/redditweaks` | [bermudalocket/Tweaks-for-Reddit](https://github.com/bermudalocket/Tweaks-for-Reddit) |
| `bitboutique/nstableview-sorting` | [stevebartholomew/NSTableView-Sorting](https://github.com/stevebartholomew/NSTableView-Sorting) |
| `branchmetrics/ios-branch-deep-linking` | [BranchMetrics/ios-branch-deep-linking-attribution](https://github.com/BranchMetrics/ios-branch-deep-linking-attribution) |
| `brentsimmons/evergreen` | [Ranchero-Software/NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire) |
| `brentsimmons/netnewswire` | [Ranchero-Software/NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire) |
| `castial/hyalertcontroller` | [iafine/HYAlertController](https://github.com/iafine/HYAlertController) |
| `changemin/cmloadingbutton` | [byunkyungmin/LoadingButton](https://github.com/byunkyungmin/LoadingButton) |
| `changemin/loadingbutton` | [byunkyungmin/LoadingButton](https://github.com/byunkyungmin/LoadingButton) |
| `codegeeker180/avfonts` | [arnavgupta180/AVFonts](https://github.com/arnavgupta180/AVFonts) |
| `codeido/pmalertcontroller` | [pmusolino/PMAlertController](https://github.com/pmusolino/PMAlertController) |
| `collinhundley/swift-ai` | [Swift-AI/Swift-AI](https://github.com/Swift-AI/Swift-AI) |
| `comyarzaheri/chronos-swift` | [comyar/Chronos-Swift](https://github.com/comyar/Chronos-Swift) |
| `comyarzaheri/tuningfork` | [comyar/TuningFork](https://github.com/comyar/TuningFork) |
| `csontosgabor/twitter_post` | [gaborcsontos/Twitter_Post](https://github.com/gaborcsontos/Twitter_Post) |
| `czechboy0/redbird` | [vapor/redis](https://github.com/vapor/redis) |
| `czechboy0/socks` | [vapor-community/sockets](https://github.com/vapor-community/sockets) |
| `cztatsumi-keisuke/tkkeyboardcontrol` | [cokaholic/TKKeyboardControl](https://github.com/cokaholic/TKKeyboardControl) |
| `danielgindi/charts` | [ChartsOrg/Charts](https://github.com/ChartsOrg/Charts) |
| `danielsaidi/keyboardkit` | [KeyboardKit/KeyboardKit](https://github.com/KeyboardKit/KeyboardKit) |
| `dcvz/dcdirectorywatcher` | [dcvz/DirectoryObserver](https://github.com/dcvz/DirectoryObserver) |
| `dehesa/metal` | [dehesa/sample-metal](https://github.com/dehesa/sample-metal) |
| `della-padula/elliotable` | [bbdyno/Elliotable](https://github.com/bbdyno/Elliotable) |
| `denheadless/transporter` | [DenTelezhkin/Transporter](https://github.com/DenTelezhkin/Transporter) |
| `dillidon/alerts-pickers` | [dillidon/alerts-and-pickers](https://github.com/dillidon/alerts-and-pickers) |
| `dinhviethoa/dejalu` | [dinhvh/dejalu](https://github.com/dinhvh/dejalu) |
| `dnstylish/swiftui-onboarding-screen-animation` | [guendev/SwiftUI-OnBoarding-Screen-Animation](https://github.com/guendev/SwiftUI-OnBoarding-Screen-Animation) |
| `docterd/playindicator` | [obrhoff/SwimplyPlayIndicator](https://github.com/obrhoff/SwimplyPlayIndicator) |
| `dzenbot/iconic` | [home-assistant/Iconic](https://github.com/home-assistant/Iconic) |
| `ebelinski/typestyle` | [tapmoko/typestyle](https://github.com/tapmoko/typestyle) |
| `elliottminns/blackfish` | [elliottminns/blackfire](https://github.com/elliottminns/blackfire) |
| `entotsu/pulltobounce` | [takuoka/PullToBounce](https://github.com/takuoka/PullToBounce) |
| `entotsu/tkanimatedcheckbutton` | [takuoka/TKAnimatedCheckButton](https://github.com/takuoka/TKAnimatedCheckButton) |
| `entotsu/tksubmittransition` | [takuoka/TKSubmitTransition](https://github.com/takuoka/TKSubmitTransition) |
| `entotsu/tkswarmalert` | [takuoka/TKSwarmAlert](https://github.com/takuoka/TKSwarmAlert) |
| `eonist/swift-utils` | [eonist/my-swift-projects](https://github.com/eonist/my-swift-projects) |
| `evnaz/enswiftsidemenu` | [devgenios/ENSwiftSideMenu](https://github.com/devgenios/ENSwiftSideMenu) |
| `exchangegroup/dodo` | [evgenyneu/Dodo](https://github.com/evgenyneu/Dodo) |
| `eyrefree/efautoscrolllabel` | [EFPrefix/EFAutoScrollLabel](https://github.com/EFPrefix/EFAutoScrollLabel) |
| `eyrefree/efcolorpicker` | [EFPrefix/EFColorPicker](https://github.com/EFPrefix/EFColorPicker) |
| `ezefranca/watchnote` | [ezefranca/watchpresenter](https://github.com/ezefranca/watchpresenter) |
| `facebook/shimmer` | [facebookarchive/Shimmer](https://github.com/facebookarchive/Shimmer) |
| `firebase/ios-swift-chat-example` | [googlearchive/ios-swift-chat-example](https://github.com/googlearchive/ios-swift-chat-example) |
| `frogg/fredkittabbarsplitview` | [riedel-wtf/FredKitTabBarSplitView](https://github.com/riedel-wtf/FredKitTabBarSplitView) |
| `garnele007/swiftocr` | [NMAC427/SwiftOCR](https://github.com/NMAC427/SwiftOCR) |
| `gaurvw/mpgtextfield` | [gwadhwani/MPGTextField](https://github.com/gwadhwani/MPGTextField) |
| `goktugyil/ezswiftextensions` | [Esqarrouth/EZSwiftExtensions](https://github.com/Esqarrouth/EZSwiftExtensions) |
| `goktugyil/ezswipecontroller` | [Esqarrouth/EZSwipeController](https://github.com/Esqarrouth/EZSwipeController) |
| `google/science-journal-ios` | [googlearchive/science-journal-ios](https://github.com/googlearchive/science-journal-ios) |
| `gtsif21/uitags` | [gtsifrikas/UITags](https://github.com/gtsifrikas/UITags) |
| `hallelujahbaby/cfnotify` | [JT501/SwiftNotify](https://github.com/JT501/SwiftNotify) |
| `hanton/hty360player` | [hanton/Fisheye](https://github.com/hanton/Fisheye) |
| `hearst-dd/objectmapper` | [tristanhimmelman/ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper) |
| `hilen/tswechat` | [lanceylai/TSWeChat](https://github.com/lanceylai/TSWeChat) |
| `hoomazoid/ctslidinguppanel` | [andriadze/CTSlidingUpPanel](https://github.com/andriadze/CTSlidingUpPanel) |
| `horizontalsystems/bank-wallet-ios` | [horizontalsystems/unstoppable-wallet-ios](https://github.com/horizontalsystems/unstoppable-wallet-ios) |
| `huemae/suggestionskit` | [AlphanumericCharactersOrSingleHyphenz/SuggestionsKit](https://github.com/AlphanumericCharactersOrSingleHyphenz/SuggestionsKit) |
| `hyperoslo/dropdowns` | [onmyway133/EasyDropdown](https://github.com/onmyway133/EasyDropdown) |
| `hyperoslo/hue` | [zenangst/Hue](https://github.com/zenangst/Hue) |
| `hyperoslo/swiftsnippets` | [onmyway133/SwiftSnippets](https://github.com/onmyway133/SwiftSnippets) |
| `i-schuetz/chartlegends` | [ivnsch/ChartLegends](https://github.com/ivnsch/ChartLegends) |
| `i-schuetz/piecharts` | [ivnsch/PieCharts](https://github.com/ivnsch/PieCharts) |
| `i-schuetz/swiftcharts` | [ivnsch/SwiftCharts](https://github.com/ivnsch/SwiftCharts) |
| `ibm-swift/kitura` | [Kitura/Kitura](https://github.com/Kitura/Kitura) |
| `ichait/awesome-osx` | [iCHAIT/awesome-macOS](https://github.com/iCHAIT/awesome-macOS) |
| `igormatyushkin014/laconic` | [simplisticated/Laconic](https://github.com/simplisticated/Laconic) |
| `igormatyushkin014/sensitive` | [simplisticated/Sensitive](https://github.com/simplisticated/Sensitive) |
| `igormatyushkin014/solid` | [simplisticated/Solid](https://github.com/simplisticated/Solid) |
| `igormatyushkin014/verbose` | [simplisticated/Verbose](https://github.com/simplisticated/Verbose) |
| `imcd23/tiltedtabview` | [ian-mcdowell/TiltedTabView](https://github.com/ian-mcdowell/TiltedTabView) |
| `imjog/animatedmasklabel` | [jogendra/LoadingShimmer](https://github.com/jogendra/LoadingShimmer) |
| `infullmobile/wobbleview` | [dotintent/WobbleView](https://github.com/dotintent/WobbleView) |
| `ink-spot/upcarouselflowlayout` | [zepojo/UPCarouselFlowLayout](https://github.com/zepojo/UPCarouselFlowLayout) |
| `inspace-io/insphotogallery` | [m1entus/INSPhotoGallery](https://github.com/m1entus/INSPhotoGallery) |
| `interactive-studio/transitionabletab` | [ParkGwangBeom/TransitionableTab](https://github.com/ParkGwangBeom/TransitionableTab) |
| `interactive-studio/windless` | [ParkGwangBeom/Windless](https://github.com/ParkGwangBeom/Windless) |
| `iospower/appstorelikeexampleswift3` | [Piyush-Sinroja/AppStoreLikeExampleSwift3](https://github.com/Piyush-Sinroja/AppStoreLikeExampleSwift3) |
| `ivanvorobei/requestpermission` | [sparrowcode/PermissionsKit](https://github.com/sparrowcode/PermissionsKit) |
| `ivanvorobei/spalert` | [sparrowcode/AlertKit](https://github.com/sparrowcode/AlertKit) |
| `ivanvorobei/sppermissions` | [sparrowcode/PermissionsKit](https://github.com/sparrowcode/PermissionsKit) |
| `iwasrobbed/down` | [johnxnguyen/Down](https://github.com/johnxnguyen/Down) |
| `jakelin/ibanimatable` | [IBAnimatable/IBAnimatable](https://github.com/IBAnimatable/IBAnimatable) |
| `jastair/snackbar-ios` | [sneiko/Snackbar-iOS](https://github.com/sneiko/Snackbar-iOS) |
| `jegumhon/urweatherview` | [Urtaq/URWeatherView](https://github.com/Urtaq/URWeatherView) |
| `jerkoch/swipecellkit` | [SwipeCellKit/SwipeCellKit](https://github.com/SwipeCellKit/SwipeCellKit) |
| `jianstm/schedule` | [luoxiu/Schedule](https://github.com/luoxiu/Schedule) |
| `joe0708/sandboxbrowser` | [aidevjoe/SandboxBrowser](https://github.com/aidevjoe/SandboxBrowser) |
| `joeblau/sensor-visualizer-kit` | [asafkorem/sensor-visualizer-kit](https://github.com/asafkorem/sensor-visualizer-kit) |
| `johnykutty/jksteppedprogressbar` | [jkmathew/JKSteppedProgressBar](https://github.com/jkmathew/JKSteppedProgressBar) |
| `jordidekock/colorblinds` | [jdekock/Colorblinds](https://github.com/jdekock/Colorblinds) |
| `jtbandes/metalbrot.playground` | [jtbandes/metalbrot-playground](https://github.com/jtbandes/metalbrot-playground) |
| `jvirus/compositional-layouts-kit` | [eleev/compositional-layouts-kit](https://github.com/eleev/compositional-layouts-kit) |
| `jvirus/drawer-view` | [eleev/drawer-view](https://github.com/eleev/drawer-view) |
| `jvirus/expandable-collection-view-kit` | [eleev/expandable-collection-view-kit](https://github.com/eleev/expandable-collection-view-kit) |
| `jvirus/flappy-fly-bird` | [eleev/flappy-fly-bird](https://github.com/eleev/flappy-fly-bird) |
| `jvirus/ios-spritekit-tic-tac-toe` | [eleev/tic-tac-toe](https://github.com/eleev/tic-tac-toe) |
| `karthironald/bodyprogress` | [karthick-mallow/BodyProgress](https://github.com/karthick-mallow/BodyProgress) |
| `kbelter/bubblepictures` | [glassipbel/BubblePictures](https://github.com/glassipbel/BubblePictures) |
| `kemcake/rsdotsview` | [remstos/RSDotsView](https://github.com/remstos/RSDotsView) |
| `kimar/himbo` | [DK1DA/Himbo](https://github.com/DK1DA/Himbo) |
| `kimar/tailor` | [Bearologics/Tailor](https://github.com/Bearologics/Tailor) |
| `kiran5232/audioequalizer` | [KiranPatelSpaceo/AudioEqualizer](https://github.com/KiranPatelSpaceo/AudioEqualizer) |
| `kiranjasvanee/kjcurveslider` | [KiranJasvanee/KJCircularSlider](https://github.com/KiranJasvanee/KJCircularSlider) |
| `kirualex/kapinfield` | [alexiscreuzot/KAPinField](https://github.com/alexiscreuzot/KAPinField) |
| `kirualex/swiftygif` | [alexiscreuzot/SwiftyGif](https://github.com/alexiscreuzot/SwiftyGif) |
| `kjpgit/fireworks` | [kjpgit/metal-fireworks](https://github.com/kjpgit/metal-fireworks) |
| `kneerajpro/playpauseanimation` | [kn-neeraj/PlayPauseAnimation](https://github.com/kn-neeraj/PlayPauseAnimation) |
| `kshin/hanabi` | [ivanlisovyi/Hanabi](https://github.com/ivanlisovyi/Hanabi) |
| `kubatru/jtsplashview` | [kubatruhlar/JTSplashView](https://github.com/kubatruhlar/JTSplashView) |
| `kylef/curassow` | [kylef-archive/Curassow](https://github.com/kylef-archive/Curassow) |
| `kzumu/elephant` | [s2mr/Elephant](https://github.com/s2mr/Elephant) |
| `lbrndnr/imagepickertraycontroller` | [lerboe/ImagePickerTrayController](https://github.com/lerboe/ImagePickerTrayController) |
| `liamscofield/heartrate` | [LiMaoAtCD/HeartRate](https://github.com/LiMaoAtCD/HeartRate) |
| `linkedin/layoutkit` | [LinkedInAttic/LayoutKit](https://github.com/LinkedInAttic/LayoutKit) |
| `liu044100/smile-lock` | [recruit-lifestyle/Smile-Lock](https://github.com/recruit-lifestyle/Smile-Lock) |
| `liuminqian/svpplytable` | [666lm/SvpplyTable](https://github.com/666lm/SvpplyTable) |
| `lkzhao/hero` | [HeroTransitions/Hero](https://github.com/HeroTransitions/Hero) |
| `loconsolutions/iosnotificationbanner` | [elarahq/iOSNotificationBanner](https://github.com/elarahq/iOSNotificationBanner) |
| `lojals/joemojiablebtn` | [lojals/ReactionButton](https://github.com/lojals/ReactionButton) |
| `lorentey/attabench` | [attaswift/Attabench](https://github.com/attaswift/Attabench) |
| `louisdh/terminal` | [louisdh/openterm](https://github.com/louisdh/openterm) |
| `lucasmucgh/bottomsheet` | [lucaszischka/BottomSheet](https://github.com/lucaszischka/BottomSheet) |
| `luiyezheng/jlstickertextview` | [Textcat/JLStickerTextView](https://github.com/Textcat/JLStickerTextView) |
| `lukakerr/twig` | [lukakerr/Pine](https://github.com/lukakerr/Pine) |
| `luubra/emojiintelligence` | [BilalReffas/EmojiIntelligence](https://github.com/BilalReffas/EmojiIntelligence) |
| `m-hamed/photo-editor` | [mhm-ibrahim/photo-editor](https://github.com/mhm-ibrahim/photo-editor) |
| `maculateconception/aural-player` | [kartik-venugopal/aural-player](https://github.com/kartik-venugopal/aural-player) |
| `mailonline/imageviewer` | [Krisiacik/ImageViewer](https://github.com/Krisiacik/ImageViewer) |
| `matryer/bitbar` | [matryer/xbar](https://github.com/matryer/xbar) |
| `mav3r1ck/orbit7` | [Aaron-A-zz/Orbit7](https://github.com/Aaron-A-zz/Orbit7) |
| `mav3r1ck/project-rainman` | [Aaron-A-zz/Project-RainMan](https://github.com/Aaron-A-zz/Project-RainMan) |
| `metrolab/curvyroute` | [seatcode/curvyRoute](https://github.com/seatcode/curvyRoute) |
| `mittsuu/mtcoordinatorview` | [mittsu333/MTCoordinatorView](https://github.com/mittsu333/MTCoordinatorView) |
| `mmrmmlrr/handytext` | [aleksey-ios-dev/HandyText](https://github.com/aleksey-ios-dev/HandyText) |
| `mobileplayer/mobileplayer-ios` | [sahin/mobileplayer-ios](https://github.com/sahin/mobileplayer-ios) |
| `mozharovsky/cvcalendar` | [CVCalendar/CVCalendar](https://github.com/CVCalendar/CVCalendar) |
| `mrigdon/mrarticleviewcontroller` | [mrigdon-zz/MRArticleViewController](https://github.com/mrigdon-zz/MRArticleViewController) |
| `mrmage/daterangepicker` | [Timing-GmbH/DateRangePicker](https://github.com/Timing-GmbH/DateRangePicker) |
| `mugunthkumar/swiftlogger` | [MKSG-MugunthKumar/SwiftLogger](https://github.com/MKSG-MugunthKumar/SwiftLogger) |
| `muukii/brightroom` | [FluidGroup/Brightroom](https://github.com/FluidGroup/Brightroom) |
| `muukii/bulk` | [FluidGroup/Bulk](https://github.com/FluidGroup/Bulk) |
| `muukii/fluidinterfacekit` | [FluidGroup/FluidInterfaceKit](https://github.com/FluidGroup/FluidInterfaceKit) |
| `muukii/nextgrowingtextview` | [FluidGroup/NextGrowingTextView](https://github.com/FluidGroup/NextGrowingTextView) |
| `necolt/swifton` | [sauliusgrigaitis/Swifton](https://github.com/sauliusgrigaitis/Swifton) |
| `nestproject/frank` | [kylef-archive/Frank](https://github.com/kylef-archive/Frank) |
| `nguyentrai2011/tnanimateslider` | [nguyenvantrai2011/TNAnimateSlider](https://github.com/nguyenvantrai2011/TNAnimateSlider) |
| `nilstack/hellovision` | [SwiftBrain/HelloVision](https://github.com/SwiftBrain/HelloVision) |
| `nodes-ios/serpent` | [ml-archive/Serpent](https://github.com/ml-archive/Serpent) |
| `nvisium/swift.nv` | [NetSPI/Swift.nV](https://github.com/NetSPI/Swift.nV) |
| `onebuffer/uiwaveview` | [bionelabs/UIWaveView](https://github.com/bionelabs/UIWaveView) |
| `onmyway133/fantastic-ios-animation` | [onmyway133/awesome-ios-animation](https://github.com/onmyway133/awesome-ios-animation) |
| `onmyway133/fantastic-ios-architecture` | [onmyway133/awesome-ios-architecture](https://github.com/onmyway133/awesome-ios-architecture) |
| `onmyway133/fantastic-machine-learning` | [onmyway133/awesome-machine-learning](https://github.com/onmyway133/awesome-machine-learning) |
| `opensesamemanager/opensesame` | [EthanLipnik/OpenSesame](https://github.com/EthanLipnik/OpenSesame) |
| `p-x9/swiftlint-xcodeplugin` | [p-x9/SwiftLintXcodePlugin](https://github.com/p-x9/SwiftLintXcodePlugin) |
| `pablojotaguardiola/app-rating-alert` | [pablojotaguardiola/AppRatingAlert-Swift](https://github.com/pablojotaguardiola/AppRatingAlert-Swift) |
| `pantuspavel/ppassetsactioncontroller` | [pavelpantus/PPAssetsActionController](https://github.com/pavelpantus/PPAssetsActionController) |
| `paulofaria/aeon` | [ZewoGraveyard/Aeon](https://github.com/ZewoGraveyard/Aeon) |
| `philackm/scrollable-graphview` | [philackm/ScrollableGraphView](https://github.com/philackm/ScrollableGraphView) |
| `piknotech/sfsafesymbols` | [SFSafeSymbols/SFSafeSymbols](https://github.com/SFSafeSymbols/SFSafeSymbols) |
| `pkpk-carnage/otresizableview` | [Frog-Frog/OTResizableView](https://github.com/Frog-Frog/OTResizableView) |
| `poolqf/fillableloaders` | [polqf/FillableLoaders](https://github.com/polqf/FillableLoaders) |
| `projectdent/arkit-corelocation` | [AndrewHartAR/ARKit-CoreLocation](https://github.com/AndrewHartAR/ARKit-CoreLocation) |
| `prynt/prynttrimmerview` | [HHK1/PryntTrimmerView](https://github.com/HHK1/PryntTrimmerView) |
| `quangpc/hqpagerviewcontroller` | [quangpc-zz/HQPagerViewController](https://github.com/quangpc-zz/HQPagerViewController) |
| `quickbirdstudios/flippingnotch` | [QuickBirdEng/FlippingNotch](https://github.com/QuickBirdEng/FlippingNotch) |
| `quickbirdstudios/pulltoreach` | [QuickBirdEng/PullToReach](https://github.com/QuickBirdEng/PullToReach) |
| `qutheory/vapor` | [vapor/vapor](https://github.com/vapor/vapor) |
| `rabbitmc/inbox-replica` | [miralem-cebic/inbox-replica](https://github.com/miralem-cebic/inbox-replica) |
| `raizlabs/bonmot` | [Rightpoint/BonMot](https://github.com/Rightpoint/BonMot) |
| `rakuyomo/jsonpreview` | [RakuyoKit/JSONPreview](https://github.com/RakuyoKit/JSONPreview) |
| `rawrjustin/bridge` | [BridgeNetworking/Bridge](https://github.com/BridgeNetworking/Bridge) |
| `raywenderlich/swift-algorithm-club` | [kodecocodes/swift-algorithm-club](https://github.com/kodecocodes/swift-algorithm-club) |
| `robbykraft/panorama` | [amkraft/Panorama](https://github.com/amkraft/Panorama) |
| `robotsandpencils/xcodesapp` | [XcodesOrg/XcodesApp](https://github.com/XcodesOrg/XcodesApp) |
| `roylee-ml/prismasimpleimagepicker` | [liangdrime/PrismaSimpleImagePicker](https://github.com/liangdrime/PrismaSimpleImagePicker) |
| `rupammitra/rmsquarepagecontrol` | [rupammitra/RMShapesPageControl](https://github.com/rupammitra/RMShapesPageControl) |
| `sadeghgoo/magictimer` | [MagicTimerFW/MagicTimer](https://github.com/MagicTimerFW/MagicTimer) |
| `saksdirect/route-composer` | [ekazaev/route-composer](https://github.com/ekazaev/route-composer) |
| `sanche21/dsfacebookimagepicker` | [daniel-sanche/DSFacebookImagePicker](https://github.com/daniel-sanche/DSFacebookImagePicker) |
| `saravananimaginea/sparkbuttondemo` | [saru2020/SparkButtonDemo](https://github.com/saru2020/SparkButtonDemo) |
| `savagesource/procreateundogesture` | [procreate/UndoGesture](https://github.com/procreate/UndoGesture) |
| `scamps88/ascalendar` | [Aku-n06/ASCalendar](https://github.com/Aku-n06/ASCalendar) |
| `shabankamell/swiftuiformvalidator` | [MalekKamel/SwiftUIFormValidator](https://github.com/MalekKamel/SwiftUIFormValidator) |
| `simformsolutions/ssspinnerbutton` | [SimformSolutionsPvtLtd/SSSpinnerButton](https://github.com/SimformSolutionsPvtLtd/SSSpinnerButton) |
| `sindresorhus/gifski-app` | [sindresorhus/Gifski](https://github.com/sindresorhus/Gifski) |
| `sindresorhus/launchatlogin` | [sindresorhus/LaunchAtLogin-Legacy](https://github.com/sindresorhus/LaunchAtLogin-Legacy) |
| `sindresorhus/preferences` | [sindresorhus/Settings](https://github.com/sindresorhus/Settings) |
| `sprint84/rfcalculatorkeyboard` | [sprint84/CalculatorKeyboard](https://github.com/sprint84/CalculatorKeyboard) |
| `starchand/mbtwitterscroll` | [martinblampied/MBTwitterScroll](https://github.com/martinblampied/MBTwitterScroll) |
| `storehouse/advance` | [timdonnelly/Advance](https://github.com/timdonnelly/Advance) |
| `strekfus/floatratingview` | [glenyi/FloatRatingView](https://github.com/glenyi/FloatRatingView) |
| `sufi-al-hussaini/swift-circlemenu` | [hu55a1n1/Swift-CircleMenu](https://github.com/hu55a1n1/Swift-CircleMenu) |
| `superpeteblaze/scalingcarousel` | [aataraxiaa/scalingcarousel](https://github.com/aataraxiaa/scalingcarousel) |
| `surayashivji/potterpics` | [surayashivji/potter-pics](https://github.com/surayashivji/potter-pics) |
| `swift-evolution/ios` | [EVOlution-App/iOS](https://github.com/EVOlution-App/iOS) |
| `swiftcrew/inshorts-view` | [SwiftCrew/ios-inshorts-view](https://github.com/SwiftCrew/ios-inshorts-view) |
| `szk-atmosphere/sacollectionviewverticalscalingflowlayout` | [marty-suzuki/SACollectionViewVerticalScalingFlowLayout](https://github.com/marty-suzuki/SACollectionViewVerticalScalingFlowLayout) |
| `szk-atmosphere/sahistorynavigationviewcontroller` | [marty-suzuki/SAHistoryNavigationViewController](https://github.com/marty-suzuki/SAHistoryNavigationViewController) |
| `szk-atmosphere/urlembeddedview` | [marty-suzuki/URLEmbeddedView](https://github.com/marty-suzuki/URLEmbeddedView) |
| `taglia3/parallaxcarousel` | [taglia3/TGLParallaxCarousel](https://github.com/taglia3/TGLParallaxCarousel) |
| `tasanobu/misen` | [tasanobu-zz/Misen](https://github.com/tasanobu-zz/Misen) |
| `tasanobu/typeddefaults` | [tasanobu-zz/TypedDefaults](https://github.com/tasanobu-zz/TypedDefaults) |
| `tekyslabpvtltd/tlfloatlabeltextfield` | [BhagyashreeMynamwar/TLFloatLabelTextField](https://github.com/BhagyashreeMynamwar/TLFloatLabelTextField) |
| `the0neyouseek/monitorcontrol` | [MonitorControl/MonitorControl](https://github.com/MonitorControl/MonitorControl) |
| `theodovgopol/simplecollectionviewbooking` | [theedov/SimpleCollectionViewBooking](https://github.com/theedov/SimpleCollectionViewBooking) |
| `thoughtbot/markoff` | [kaishin/markoff](https://github.com/kaishin/markoff) |
| `tomekb/postmanager` | [tombaranowicz/PostManager](https://github.com/tombaranowicz/PostManager) |
| `toygar/videothumbview` | [svhawks/VideoThumbnailViewKit](https://github.com/svhawks/VideoThumbnailViewKit) |
| `toygard/videosplash` | [sahin/VideoSplashKit](https://github.com/sahin/VideoSplashKit) |
| `tranchuong/pixcolor` | [chuongtrh/PixColor](https://github.com/chuongtrh/PixColor) |
| `twicketapp/twicketsegmentedcontrol` | [polqf/TwicketSegmentedControl](https://github.com/polqf/TwicketSegmentedControl) |
| `twolivesleft/menu` | [simsaens/Menu](https://github.com/simsaens/Menu) |
| `tylerwhitedesign/metalpinch` | [AlchemicalBytes/MetalPinch](https://github.com/AlchemicalBytes/MetalPinch) |
| `uacaps/pagemenu` | [PageMenu/PageMenu](https://github.com/PageMenu/PageMenu) |
| `varabeis/splarkcontroller` | [ivanvorobei/SPLarkController](https://github.com/ivanvorobei/SPLarkController) |
| `varshylmobile/vmfloatlabel` | [jimmyjose-dev/VMFloatLabel](https://github.com/jimmyjose-dev/VMFloatLabel) |
| `victorchu8/rival` | [vctrchu/Rival](https://github.com/vctrchu/Rival) |
| `viwid/evergreen` | [nilsvu/Evergreen](https://github.com/nilsvu/Evergreen) |
| `vladaverin24/dynamicbubble` | [0xNSHuman/DynamicBubble](https://github.com/0xNSHuman/DynamicBubble) |
| `wangjwchn/jwanimatedimage` | [wangjwchn/AImage](https://github.com/wangjwchn/AImage) |
| `wenghengcong/coderpursue` | [wenghengcong/BeeFun-Pro](https://github.com/wenghengcong/BeeFun-Pro) |
| `wetransfer/wescan` | [WeTransferArchive/WeScan](https://github.com/WeTransferArchive/WeScan) |
| `whatsltd4us/vtswiftyslidemenu` | [vinhnotes/VTSwiftySlideMenu](https://github.com/vinhnotes/VTSwiftySlideMenu) |
| `wizeline/wlemptystate` | [WizelineLabs/WLEmptyState](https://github.com/WizelineLabs/WLEmptyState) |
| `wojteklukaszuk/watchdog` | [wojteklu/Watchdog](https://github.com/wojteklu/Watchdog) |
| `xhacker/taglistview` | [ElaWorkshop/TagListView](https://github.com/ElaWorkshop/TagListView) |
| `xhamr/fave-button` | [janselv/fave-button](https://github.com/janselv/fave-button) |
| `yarodevuci/vkmusic` | [yarodevuci/Muzonchik](https://github.com/yarodevuci/Muzonchik) |
| `yoomoney-tech/mobile-analytics-chart-swift` | [yoomoney/mobile-analytics-chart-swift](https://github.com/yoomoney/mobile-analytics-chart-swift) |
| `yr/cachyr` | [nrkno/yr-cachyr](https://github.com/nrkno/yr-cachyr) |
| `yukiasai/gecco` | [xai3/Gecco](https://github.com/xai3/Gecco) |
| `yukiasai/minamo` | [xai3/Minamo](https://github.com/xai3/Minamo) |
| `yukiasai/nori` | [xai3/Nori](https://github.com/xai3/Nori) |
| `zandew/minimusicwidget` | [Zandew/Oracle](https://github.com/Zandew/Oracle) |
| `zewo/luminescence` | [ZewoGraveyard/HTTPParser](https://github.com/ZewoGraveyard/HTTPParser) |

## Consolidated duplicates

Each canonical resource now has one entry. Tags and the more informative description were retained when merging duplicates.

| Canonical source | Category of duplicate entry | Retained topic |
| --- | --- | --- |
| https://github.com/andreamazz/SubtleVolume | Utils | Audio |
| https://github.com/BeauNouvelle/FaceAware | Image | Images |
| https://github.com/byunkyungmin/LoadingButton | Button SwiftUI | Buttons |
| https://github.com/dekatotoro/SlideMenuControllerSwift | ViewController Transition | Menus |
| https://github.com/dillidon/alerts-and-pickers | Alert | Alerts and notifications |
| https://github.com/dingwilson/SwiftVideoBackground | Video | Asset pickers |
| https://github.com/dkhamsing/open-source-ios-apps | Other Lists | Resource lists |
| https://github.com/dkhamsing/open-source-ios-apps | App | Resource lists |
| https://github.com/DragonCherry/AssetsPickerViewController | Asset Picker | Asset pickers |
| https://github.com/EFPrefix/EFColorPicker | Color | Asset pickers |
| https://github.com/gaetanzanella/OverlayContainer | Panel | Panels and bottom sheets |
| https://github.com/HarshilShah/DeckTransition | ViewController Transition | Panels and bottom sheets |
| https://github.com/home-assistant/Iconic | Resource | Fonts and icons |
| https://github.com/huri000/SwiftEntryKit | Alert | Alerts and notifications |
| https://github.com/hyperoslo/ImagePicker | Asset Picker | Asset pickers |
| https://github.com/hyperoslo/Whisper | Alert | Alerts and notifications |
| https://github.com/iCHAIT/awesome-macOS | Other Lists | Resource lists |
| https://github.com/ivanvorobei/SPStorkController | ViewController Transition | Panels and bottom sheets |
| https://github.com/james01/CardNavigation | ViewController Transition | Navigation bars |
| https://github.com/josejuanqm/VersaPlayer | Video | Apps and sample projects |
| https://github.com/kaandedeoglu/KDCircularProgress | Progress Bar | Loading indicators |
| https://github.com/ltebean/Live | App | Apps and sample projects |
| https://github.com/luispadron/LPThumbnailView | View | Images |
| https://github.com/marcosgriselli/ViewAnimator | ViewController Transition | View controller transitions |
| https://github.com/MarioIannotta/MIBlurPopup | ViewController Transition | Panels and bottom sheets |
| https://github.com/mathcarignani/MCMHeaderAnimated | ViewController Transition | Table views |
| https://github.com/PageMenu/PageMenu | PageControl | Menus |
| https://github.com/polqf/FillableLoaders | Progress Bar | Loading indicators |
| https://github.com/Ramotion/preview-transition | ViewController Transition | Asset pickers |
| https://github.com/Ranchero-Software/NetNewsWire | App macOS | macOS apps |
| https://github.com/rechsteiner/Parchment | TableView | Tab bars |
| https://github.com/serhii-londar/open-source-mac-os-apps | App macOS | Resource lists |
| https://github.com/sparrowcode/PermissionsKit | Permission | Permissions |
| https://github.com/suzuki-0000/SKPhotoBrowser | CollectionView | Asset pickers |
| https://github.com/Textcat/JLStickerTextView | Text | Images |
| https://github.com/WenchaoD/FSPagerView | Pager | Collection views |
