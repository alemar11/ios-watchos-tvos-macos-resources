# Swift resources for iOS, macOS, tvOS and watchOS

Libraries, frameworks, tools and example projects for Apple platforms, plus server-side Swift.
Browse by purpose below; entries within each topic are sorted alphabetically and each resource is listed once.

## How to use this list

- **Platform tags:** `iOS`, `macOS`, `tvOS`, `watchOS`, `visionOS`.
- **UI framework tags:** `SwiftUI`, `UIKit`, `AppKit`. SwiftUI resources appear alongside other implementations of the same feature.
- **Status:** `Archived` means the owner has archived the GitHub repository. These resources remain available for reference.
- Tags reflect existing catalogue annotations, explicit descriptions and author-supplied repository topics. They are discovery aids, not an exhaustive compatibility matrix; missing tags do not mean lack of support.
- Availability does not establish active maintenance or compatibility with current Swift and Xcode. Check the project's README, requirements and releases before adopting it.

Last availability audit: **2026-10-04**. See [audit results and exceptions](docs/link-audit.md) and [contribution and validation instructions](CONTRIBUTING.md).

## Contents

| Area | Topics |
| --- | --- |
| [Apps and examples](#apps-and-examples) | [Apps and sample projects](#apps-and-sample-projects) · [macOS apps](#macos-apps) · [UI design examples](#ui-design-examples) |
| [UI foundations](#ui-foundations) | [Layout](#layout) · [UI frameworks](#ui-frameworks) · [View controllers](#view-controllers) · [Views](#views) |
| [Controls and input](#controls-and-input) | [Badges](#badges) · [Buttons](#buttons) · [Checkboxes and switches](#checkboxes-and-switches) · [Contacts pickers](#contacts-pickers) · [Controls](#controls) · [Dates and calendars](#dates-and-calendars) · [Gestures](#gestures) · [Keyboards](#keyboards) · [Pickers](#pickers) · [Ratings](#ratings) · [Segmented controls](#segmented-controls) · [Sliders](#sliders) · [Steppers](#steppers) · [Tags and tokens](#tags-and-tokens) · [Text fields and forms](#text-fields-and-forms) |
| [Lists and scrolling](#lists-and-scrolling) | [Collection views](#collection-views) · [Pull to refresh](#pull-to-refresh) · [Scroll views](#scroll-views) · [Table views](#table-views) |
| [Navigation and presentation](#navigation-and-presentation) | [Action sheets](#action-sheets) · [Alerts and notifications](#alerts-and-notifications) · [Cards](#cards) · [Menus](#menus) · [Navigation bars](#navigation-bars) · [Onboarding](#onboarding) · [Page indicators](#page-indicators) · [Pagers](#pagers) · [Panels and bottom sheets](#panels-and-bottom-sheets) · [Routing and deep links](#routing-and-deep-links) · [Sharing](#sharing) · [Tab bars](#tab-bars) · [Toolbars](#toolbars) |
| [Animation and feedback](#animation-and-feedback) | [Animations](#animations) · [Loading indicators](#loading-indicators) · [Physics and dynamics](#physics-and-dynamics) · [Progress indicators](#progress-indicators) · [View controller transitions](#view-controller-transitions) |
| [Graphics and typography](#graphics-and-typography) | [Charts](#charts) · [Colors](#colors) · [Fonts and icons](#fonts-and-icons) · [Geometry and drawing](#geometry-and-drawing) · [Labels](#labels) · [Text and rich text](#text-and-rich-text) |
| [Media and communication](#media-and-communication) | [Asset pickers](#asset-pickers) · [Audio](#audio) · [Images](#images) · [Messaging](#messaging) · [Speech recognition](#speech-recognition) · [Video](#video) · [Web views and previews](#web-views-and-previews) |
| [Data and infrastructure](#data-and-infrastructure) | [Architecture](#architecture) · [Concurrency](#concurrency) · [Dates and scheduling](#dates-and-scheduling) · [Files and compression](#files-and-compression) · [JSON and serialization](#json-and-serialization) · [Networking](#networking) · [Parsing and formatting](#parsing-and-formatting) · [Persistence and caching](#persistence-and-caching) · [Server-side Swift](#server-side-swift) |
| [System integration](#system-integration) | [Bluetooth and beacons](#bluetooth-and-beacons) · [Device information](#device-information) · [Localization](#localization) · [Maps and location](#maps-and-location) · [Payments](#payments) · [Permissions](#permissions) · [Security](#security) |
| [Games and machine learning](#games-and-machine-learning) | [Augmented reality](#augmented-reality) · [GameplayKit](#gameplaykit) · [Machine learning](#machine-learning) · [Metal](#metal) · [SceneKit](#scenekit) · [SpriteKit](#spritekit) |
| [Platform extensions](#platform-extensions) | [Dock](#dock) · [Menu bar](#menu-bar) · [Screensavers](#screensavers) · [Watch faces](#watch-faces) · [Widgets](#widgets) · [Windows](#windows) |
| [Developer tools](#developer-tools) | [Asset and code generation](#asset-and-code-generation) · [Logging and debugging](#logging-and-debugging) · [Scripting and command-line tools](#scripting-and-command-line-tools) · [Testing](#testing) · [Xcode extensions](#xcode-extensions) |
| [Learning and utilities](#learning-and-utilities) | [Playgrounds and snippets](#playgrounds-and-snippets) · [Resource lists](#resource-lists) · [Swift extensions and utilities](#swift-extensions-and-utilities) |

## Apps and examples

### Apps and sample projects

- [ACHNBrowserUI](https://github.com/Dimillian/ACHNBrowserUI) - The best Animal Crossing New Horizons companion app! `iOS` `SwiftUI`
- [AdguardForiOS](https://github.com/AdguardTeam/AdguardForiOS) - The most advanced Safari content blocker and privacy keeper for iOS. `iOS`
- [AKAudioOverlap](https://github.com/piyushghoghari08/AKAudioOverlap) - AKAudioOverlap is audio recording, convert audio to wavefoem, overlap two audio and export/ save into local device.
- [AppStoreLikeExampleSwift3](https://github.com/Piyush-Sinroja/AppStoreLikeExampleSwift3) - Using CollectionView, UITableView, ScrollView, Such As AppStore.
- [AudioKitSynthOne](https://github.com/AudioKit/AudioKitSynthOne) - AudioKit Synth One: Open-Source iOS Synthesizer App.
- [BeeFun-Pro](https://github.com/wenghengcong/BeeFun-Pro) - Github client for iOS in Swift. `iOS`
- [BodyProgress](https://github.com/karthick-mallow/BodyProgress) - Simple workout and progress tracking app for fitness freaks with Widget support. `SwiftUI`
- [BookPlayer](https://github.com/TortugaPower/BookPlayer) - Player for your DRM-free audiobooks. `iOS`
- [breadwallet](https://github.com/breadwallet/breadwallet-ios) - The iOS version of the Bread bitcoin wallet.
- [Celestial](https://github.com/eonist/Celestial) - A delightful weather app. `iOS`
- [Charter](https://github.com/matthewpalmer/Charter) - A Swift mailing list client for iPhone and iPad.
- [Cherry](https://github.com/kenshin03/Cherry) - Mini Pomodoro Timer app designed for the  Watch. Written in Swift. `watchOS`
- [Clendar](https://github.com/vinhnx/Clendar) - Calendar app. `iOS` `macOS` `watchOS` `SwiftUI`
- [compass](https://github.com/zntfdr/Compass/tree/master/compass) - A Minimal Compass iOS App 🧭 `iOS` `Archived`
- [ConvertCurrency](https://github.com/gkye/ConvertCurrency) - An iOS app for converting currencies written in Swift3. `Archived`
- [CoronaTracker](https://github.com/mhdhejazi/CoronaTracker) - Coronavirus tracker app for iOS & macOS with maps & charts. `iOS`
- [CoronaVirusTracker](https://github.com/alfianlosari/CoronaVirusTrackerSwiftUI) - Corona Virus Tracker & Advices iOS App with SwiftUI. `SwiftUI`
- [DesignerNewsApp](https://github.com/MengTo/DesignerNewsApp) - Build a Swift App as a designer.
- [Doro](https://github.com/codeOfRobin/doro) - Pomodoro app.
- [Dunk](https://github.com/naoyashiga/Dunk) - Dunk is Dribbble client. `iOS`
- [EventBlankApp](https://github.com/icanzilb/EventBlankApp) - A free open source iOS app for events or conferences.
- [flappy-fly-bird](https://github.com/eleev/flappy-fly-bird) - Flappy Fly-Bird is an iOS/SpriteKit game written using the latest verion of Swift programming language and GameplayKit.
- [Giovanni](https://github.com/gabrieloc/GIOVANNI) - A Gameboy Emulator for the Apple Watch. `watchOS`
- [GitHawk](https://github.com/GitHawkApp/GitHawk) - A GitHub project manager app for iOS. `iOS` `Archived`
- [GrandCentralBoard](https://github.com/macoscope/GrandCentralBoard) - Hang a TV in your open space or team room to show everyone what's up and get them up to speed. `tvOS`
- [gulps](https://github.com/FancyPixel/gulps) - Gulps is an open source app for iOS and Apple Watch that lets you keep track of your daily water consumption. `Archived`
- [Hackery](https://github.com/timshim/Hackery) - A HackerNews client made using SwiftUI. `SwiftUI`
- [headlines-iOS](https://github.com/Canillitapp/headlines-iOS)
- [Hoopy](https://github.com/danielinoa/Hoopy) - Hoopy is a lightweight and minimal Dribbble client. `Archived`
- [iCopyPasta](https://github.com/alltheflow/iCopyPasta) - iOS app for your pasteboard feed, demo app for experimenting with RxSwift.
- [Icro](https://github.com/hartlco/Icro) - Icro, a third-party micro.blog client.
- [Image-to-Ascii-Art](https://github.com/liamrosenfeld/Image-to-Ascii-Art) - An iOS app that can turn any image into ascii art.
- [ImageGallery](https://github.com/ashishbl86/ImageGallery) - This is an iPad only app, where you can drag in images from other apps and save them into image galleries. This app uses UIKit's UIDocument to store the image galleries as documents. `iOS` `UIKit`
- [insights-for-instagram](https://github.com/adimango/insights-for-instagram) - A simple iOS Instagram's media insights App written in Swift 4.
- [Instagram_Stories](https://github.com/drawRect/Instagram_Stories) - Inspired by Instagram Stories functionality. This source is similar to Instagram Stories which is having both image and video support. `iOS` `Archived`
- [ios-mail](https://github.com/ProtonMail/ios-mail) - Secure email that protects your privacy
- [ish](https://github.com/ish-app/ish) - A project to get a Linux shell running on iOS, using usermode x86 emulation and syscall translation. `iOS`
- [kickstarter App](https://github.com/kickstarter/ios-oss) - Kickstarter for iOS. Bring new ideas to life, anywhere. `iOS`
- [ladybug](https://github.com/ethanhuang13/ladybug) - Handle rdar:// links gracefully. `iOS`
- [Live](https://github.com/ltebean/Live) - Demonstrate how to build a live broadcast app.
- [Llitgi](https://github.com/xmollv/Llitgi) - A simple & lightweight Pocket client for iOS. `iOS` `Archived`
- [lockdown-ios](https://github.com/confirmedcode/Lockdown-iOS) - Lockdown is an Open Source and free firewall for your iOS device.
- [MovieSwiftUI](https://github.com/Dimillian/MovieSwiftUI) - MovieSwiftUI is an application that uses the MovieDB API and is built with SwiftUI. It demos some SwiftUI (& Combine) concepts. `SwiftUI`
- [MultiScreenApp](https://github.com/vedantapps/MultiScreenApp) - An app that uses Multipeer Connectivity to play a video across 6 different iOS screens with an additional phone acting as a Main/Control phone.
- [NineAnimator](https://github.com/SuperMarcus/NineAnimator) - A simple yet elegant way of waching anime on your favorite anime websites. `iOS` `macOS` `Archived`
- [Notepad](https://github.com/ruddfawcett/Notepad) - A fully themeable markdown editor with live syntax highlighting. `iOS`
- [ODEON](https://github.com/Sherlouk/Odeon) - Beam for Reddit.
- [OneHourWalker](https://github.com/appcoda/OneHourWalker) - HealthKit demo app.
- [openterm](https://github.com/louisdh/openterm) - OpenTerm, a sandboxed command line interface for iOS `iOS` `Archived`
- [Oracle](https://github.com/Zandew/Oracle) - Minimalistic music player and playlist builder. Recommends songs using tone analyzer.
- [photostickers](https://github.com/jjochen/photostickers) - iOS Photo Stickers App.
- [photostream](https://github.com/mownier/photostream) - A photo sharing iOS app that uses Firebase and is being driven by VIPER architecture. `iOS`
- [Pisth](https://github.com/ColdGrub1384/Pisth) - SSH and SFTP client for iOS. `iOS`
- [pixelino](https://github.com/melloskitten/pixelino) - Pixel-drawing app for iOS. `iOS`
- [PixPic](https://github.com/Yalantis/PixPic) - PixPic, a Photo Editing App.
- [pokemon-weakness-ios](https://github.com/pokeweak/pokemon-weakness-ios) - Source code for Pokemon Weakness iOS application.
- [Portrait-without-Depth-ios](https://github.com/koooootake/Portrait-without-Depth-ios) - try! Swift 2019 demo app that converts Depth-less 2D images into Portrait mode.
- [PostManager](https://github.com/tombaranowicz/PostManager) - iOS Swift + Node.js app to manage and schedule twitter posts (like buffer).
- [potter-pics](https://github.com/surayashivji/potter-pics) - harry potter themed social network similar to IG `iOS`
- [Project-RainMan](https://github.com/Aaron-A-zz/Project-RainMan) - Open Source Weather App created with Swift.
- [Red Zebra](https://github.com/JKKross/red_zebra) - Minimalist text/code editor for iOS. `iOS` `Archived`
- [reddit-swiftui](https://github.com/carson-katri/reddit-swiftui) - A cross-platform Reddit client built in SwiftUI. `iOS` `macOS` `watchOS` `SwiftUI`
- [ReviewTime](https://github.com/nthegedus/ReviewTime) - Review Time is an open source app for iOS written in Swift that show the average review times for iOS and the Mac Apps using data crowdsourced from AppReviewTime.
- [Rival](https://github.com/vctrchu/Rival) - A fitness iOS application that allows users to track, view and compete against friends. Built with Swift and Firebase.
- [Science Journal by Google](https://github.com/googlearchive/science-journal-ios) - Use the sensors in your mobile devices to perform science experiments. Science doesn’t just happen in the classroom or lab—tools like Science Journal let you see how the world works with just your phone. `iOS` `Archived`
- [Sentiments](https://github.com/kyleweiner/Sentiments) - Sentiments is an iOS app written in Swift that analyzes text for positive or negative sentiment.
- [SF-Viewer](https://github.com/aaronpearce/SF-Viewer) - SF Viewer is the best way to view, compare and export SF Symbols on your iOS device. `Archived`
- [simplenote-ios](https://github.com/Automattic/simplenote-ios) - Simplenote for iOS.
- [siskin-im](https://github.com/tigase/siskin-im) - Public Project of Tigase Messenger for iOS devices based on Tigase Swift XMPP library. `iOS`
- [summon](https://github.com/eonist/Summon) - Summon a person to your exact location in a building.
- [Swiflytics](https://github.com/aciidgh/Swiflytics) - Live Google Analytics.
- [Swift Evolution](https://github.com/EVOlution-App/iOS) - An iOS version of Swift Evolution.
- [Swift-Radio-Pro](https://github.com/swiftcodex/Swift-Radio-Pro) - Swift Radio is an open source radio station app with robust and professional features.
- [SwiftHN](https://github.com/Dimillian/SwiftHN) - A Hacker News reader in Swift.
- [tic-tac-toe](https://github.com/eleev/tic-tac-toe) - 🕹 iOS game - classic Tic Tac Toe with AI and state machines \[Swift + SpriteKit + GameplayKit\]. `iOS`
- [Tiktok-Clone](https://github.com/dks333/Tiktok-Clone) - iOS Tiktok Clone built with Swift. `Archived`
- [TriangleDraw](https://github.com/triangledraw/TriangleDraw-iOS) - TriangleDraw is brilliant for sketching logos. You can quickly create designs that can be used for branding on letterheads or on your website. `iOS` `Archived`
- [Tropos](https://github.com/thoughtbot/Tropos) - Weather and Forecasts for Humans. `iOS`
- [TSWeChat](https://github.com/lanceylai/TSWeChat) - A WeChat alternative. Written in Swift.
- [Tweetometer](https://github.com/BalestraPatrick/Tweetometer) - An app to see who is tweeting in your timeline.
- [typestyle](https://github.com/tapmoko/typestyle) - A native Swift iOS app that generates text with funky 𝕤𝕥𝕪𝕝𝕖𝕤 and ıllıllı decorations ıllıllı `iOS`
- [unstoppable-wallet-ios](https://github.com/horizontalsystems/unstoppable-wallet-ios) - Multi-wallet for Bitcoin, Ethereum, Binance Smart Chain and other emerging blockchains. Non-custodial storage, decentralized exchange, and extensive analytics for thousands of tokens and NFTs. Implemented on Swift.
- [Unwrap](https://github.com/twostraws/Unwrap) - Learn Swift interactively on your iPhone. `iOS`
- [v2ex](https://github.com/darkerk/v2ex) - The unofficial V2EX app for iOS. `iOS` `Archived`
- [VisualProgrammingLanguage](https://github.com/NathanFlurry/VisualProgrammingLanguage) - Visual programming language written in Swift that assembles to executable Swift code. `iOS`
- [VKMusic](https://github.com/ilyahal/VKMusic) - The app is designed for listening to music from vk.com. `Archived`
- [VoiceMemosClone](https://github.com/HassanElDesouky/VoiceMemosClone) - A clone for Apple's Voice Memos app. `Archived`
- [WatchKit-Apps](https://github.com/kostiakoval/WatchKit-Apps) - Tutorials app for WatchKit. `watchOS`
- [watchpresenter](https://github.com/ezefranca/watchpresenter) - Control Keynote using Apple Watch. `watchOS`
- [water-reminder-swiftui](https://github.com/caiobzen/water-reminder-swiftui) - A simple Apple Watch app to remind you to drink water! `watchOS` `SwiftUI`
- [weight-tracker](https://github.com/Jackson-S/weight-tracker) - iOS and watchOS weight entry app for HealthKit. `iOS` `watchOS`
- [Wire](https://github.com/wireapp/wire-ios) - Wire iOS client (iPhone and iPad). `iOS`
- [Yep](https://github.com/CatchChat/Yep) - A community where geniuses meet. `Archived`
- [youtube-iOS](https://github.com/aslanyanhaik/youtube-iOS) - youtube iOS app template written in swift 3. `iOS`

### macOS apps

- [AppWage](https://github.com/hankinsoft/AppWage) - iTunes connect reporting tool. `macOS`
- [aural-player](https://github.com/kartik-venugopal/aural-player) - Aural Player is an audio player application for the macOS platform, that was inspired by the classic Winamp player for Windows. `macOS` `Archived`
- [BandwidthLimiter](https://github.com/kishikawakatsumi/BandwidthLimiter) - The Mac application can quickly put a bandwidth limit on the network from the menu bar. `macOS`
- [BatteryNotifier](https://github.com/Kalvin126/BatteryNotifier) - OS X tool that warns you if your iOS devices needs a charge. `macOS`
- [brisk](https://github.com/br1sk/brisk) - A macOS app for submitting radars. `macOS`
- [cleartext-mac](https://github.com/mortenjust/cleartext-mac) - A text editor that only allows the top 1000 most common words in English. `macOS`
- [Clipinio](https://github.com/benjohnde/Clipinio) - Lightweight clipboard manager for OSX. `macOS` `Archived`
- [Clipy](https://github.com/Clipy/Clipy) - Clipboard extension app for Mac OSX. `macOS`
- [cloudy](https://github.com/calebd/cloudy) - Simple Overcast app for OS X. `macOS` `Archived`
- [Code Edit](https://github.com/CodeEditApp/CodeEdit) - CodeEdit is a code editor built by the community, for the community, written entirely and unapologetically for macOS. `iOS` `macOS` `SwiftUI` `AppKit`
- [CoinPriceBar](https://github.com/T-Pham/CoinPriceBar) - Cryptocurrency prices on MacBook Touch Bar. `macOS`
- [ControlRoom](https://github.com/twostraws/ControlRoom) - Control Room is a macOS app that lets you control the simulators for iOS, tvOS, and watchOS – their UI appearance, status bar configuration, and more. It wraps Apple’s own simctl command-line tool, so you’ll need Xcode installed. `macOS` `SwiftUI`
- [CopyPasta](https://github.com/alltheflow/CopyPasta) - Pasteboard feed Mac app. `macOS`
- [CotEditor](https://github.com/coteditor/CotEditor) - CotEditor is a lightweight plain-text editor for macOS. `macOS`
- [Crescendo](https://github.com/SuprHackerSteve/Crescendo) - Crescendo is a swift based, real time event viewer for macOS. It utilizes Apple's Endpoint Security Framework. `macOS`
- [dejalu](https://github.com/dinhvh/dejalu) - Fast and Simple Email Client. `macOS`
- [dshb](https://github.com/beltex/dshb) - OS X system monitor in Swift. `macOS`
- [Eul](https://github.com/gao-sun/eul) - macOS status bar. `macOS` `SwiftUI`
- [EventfulMac](https://github.com/JacobCho/EventfulMac) - OSX application that searches for events within an area using the Eventful API. `macOS`
- [fsnotes](https://github.com/glushchenko/fsnotes) - Notes manager for macOS/iOS. `iOS` `macOS`
- [gifski](https://github.com/sindresorhus/Gifski) - 🌈 Convert videos to high-quality GIFs on your Mac `macOS` `SwiftUI`
- [Gitee](https://github.com/Nightonke/Gitee) - Gitee, OS X status bar application for Github. `macOS`
- [hidden](https://github.com/dwarvesf/hidden) - A ultra-light MacOS utility that helps hide menu bar icons. `macOS`
- [hush](https://github.com/oblador/hush) - Block nags to accept cookies and privacy invasive tracking in Safari. `macOS` `SwiftUI`
- [Jukebox](https://github.com/Jaysce/Jukebox) - Jukebox is a macOS application that allows you to display and control the currently playing song from Spotify in the menu bar. `macOS` `SwiftUI`
- [localizations](https://github.com/e7711bbear/Localizations) - OS X app that manages localizations of Xcode projects. `macOS`
- [MacAssistant](https://github.com/vanshg/MacAssistant) - Google Assistant for macOS! `macOS`
- [Markoff](https://github.com/kaishin/markoff) - A light-weight Markdown (CommonMark) previewer for OSX. `macOS`
- [markr](https://github.com/lukakerr/markr) - Minimalistic markdown editor for MacOS with live preview. `macOS`
- [MonitorControl](https://github.com/MonitorControl/MonitorControl) - Control your external monitor brightness & volume on your Mac. `macOS`
- [NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire) - RSS reader for macOS and iOS. `iOS` `macOS`
- [OnlySwitch](https://github.com/jacklandrin/OnlySwitch) - OnlySwitch provides a series of toggle switches to simply your routine work. `macOS` `SwiftUI`
- [OpenSesame](https://github.com/EthanLipnik/OpenSesame) - Native and encrypted password manager for iOS and macOS. `iOS` `macOS` `SwiftUI` `Archived`
- [OpenSim](https://github.com/luosheng/OpenSim) - OpenSim is an open source alternative for SimPholders, written in Swift. `macOS`
- [osx-xliff-tool](https://github.com/remuslazar/osx-xliff-tool) - OS X Application for editing XLIFF files generated by Xcode. `macOS`
- [pareto-mac](https://github.com/ParetoSecurity/pareto-mac) - Security checklist app for your Mac. `macOS` `SwiftUI`
- [Pasty](https://github.com/rawnly/Pasty) - Live clipboard viewer. `iOS` `macOS`
- [PDF-Archiver](https://github.com/PDF-Archiver/PDF-Archiver) - Archive all incoming documents digitally to access and search them in an easier way. Transfer the sorted documents to your smartphone or make a backup within seconds. `macOS`
- [Pine](https://github.com/lukakerr/Pine) - A modern, native macOS markdown editor `macOS`
- [producthunt-osx](https://github.com/producthunt/producthunt-osx) - The best new products, every day on Mac. `macOS` `Archived`
- [reminders-menubar](https://github.com/DamascenoRafael/reminders-menubar) - Simple macOS menu bar app to view and interact with reminders. `macOS` `SwiftUI`
- [Roar](https://github.com/tylerhall/roar) - Let's reskin Notification Center. `macOS`
- [Screenotate](https://github.com/osnr/Screenotate) - Automatically annotate your screenshots. `macOS`
- [Spaceman](https://github.com/Jaysce/Spaceman) - Spaceman is an application for macOS that allows you to view your Spaces / Virtual Desktops in the menu bar. `macOS`
- [StackOv](https://github.com/surfstudio/StackOv) -  StackOverflow reader. `iOS` `macOS` `SwiftUI`
- [Sweetcorn](https://github.com/FlexMonkey/sweetcorn) - Node based CIKernel creation. `macOS`
- [Tailor](https://github.com/Bearologics/Tailor) - An OS X status bar app to quickly check for new releases at Swift.org. `macOS` `Archived`
- [Trailer](https://github.com/ptsochantaris/trailer) - Managing Pull Requests and Issues For GitHub & GitHub Enterprise. `iOS` `macOS` `watchOS`
- [Tweaks-for-Reddit](https://github.com/bermudalocket/Tweaks-for-Reddit) - A Safari App Extension to help make Reddit suck just a little less on Safari 13+. Written (mostly) in SwiftUI. `macOS` `SwiftUI` `Archived`
- [Up-Down](https://github.com/gjiazhe/Up-Down) - A menu bar widget for OS X that monitors upload and download speeds. `macOS`
- [WWDC](https://github.com/insidegui/WWDC) - WWDC app for OS X. `macOS`
- [xbar](https://github.com/matryer/xbar) - Put the output from any script or program into your macOS Menu Bar (the BitBar reboot)
- [xcode-dev-cleaner](https://github.com/vashpan/xcode-dev-cleaner) - If you want to reclaim tens of gigabytes of your storage used for various Xcode caches - this tool is for you! `macOS`
- [XcodesApp](https://github.com/XcodesOrg/XcodesApp) - The easiest way to install and switch between multiple versions of Xcode. `macOS` `SwiftUI`
- [xi-mac](https://github.com/xi-editor/xi-mac) - The xi-editor mac frontend. `macOS`

### UI design examples

- [Building custom UI elements with IBDesignable](https://www.thinkandbuild.it/building-custom-ui-element-with-ibdesignable/)
- [Design_to_code](https://github.com/dheerajghub/Design_to_code) - This is a series of design that i randomly took from various instagram, facebook pages and try to convert thoes designs into code hope it helps you. `iOS` `UIKit`
- [InstagramRedesignConcept](https://github.com/rphlfc/InstagramRedesignConcept) - Redesign do Instagram para desktop e mobile com SwiftUI `SwiftUI`
- [SwiftUI-by-Examples](https://github.com/artemnovichkov/SwiftUI-by-Examples) - Examples of new SwiftUI framework. `SwiftUI`
- [swiftui.builds](https://github.com/FranckNdame/swiftui.builds) - Building cool stuff in SwiftUI. `SwiftUI`
- [TelegramRedesign](https://github.com/rphlfc/TelegramRedesign) `SwiftUI`
- [UrbanVillageProjectScreens](https://github.com/claudiaeng/UrbanVillageProjectScreens) - Pretty iOS mobile screens + AVPlayer video view. `iOS` `SwiftUI`

## UI foundations

### Layout

- [KGNAutoLayout](https://github.com/kgn/KGNAutoLayout) - Making AutoLayout Easy. `iOS` `UIKit`
- [LayoutKit](https://github.com/LinkedInAttic/LayoutKit) - LayoutKit is a fast view layout library for iOS. `iOS` `macOS` `tvOS` `Archived`
- [Nori](https://github.com/xai3/Nori) - Easier to apply code based style guide to storyboard.
- [SizeClasser](https://github.com/cemolcay/SizeClasser) - Device specific UITraitCollection helper with split view detection for iOS.
- [SnapKit](https://github.com/SnapKit/SnapKit) - A Swift Autolayout DSL for iOS & OS X.
- [texture](https://github.com/TextureGroup/Texture) - Smooth asynchronous user interfaces for iOS apps. `UIKit`
- [TinyConstraints](https://github.com/roberthein/TinyConstraints) - Nothing but sugar.

### UI frameworks

- [Material](https://github.com/CosmicMind/Material) - A beautiful graphics framework for Material Design in Swift. `iOS`
- [material-components-ios](https://github.com/material-components/material-components-ios) - Modular and customizable Material Design UI components for iOS. `iOS` `Archived`
- [SwiftUI-Introspect](https://github.com/siteline/swiftui-introspect) - Introspect allows you to get the underlying UIKit or AppKit element of a SwiftUI view. `SwiftUI` `UIKit` `AppKit`
- [SwiftUIX](https://github.com/SwiftUIX/SwiftUIX) - An extension to the standard SwiftUI library. `iOS` `macOS` `visionOS` `SwiftUI`

### View controllers

- [AMLoginSignup](https://github.com/amirdew/AMLoginSignup) - Login/Signup ViewController for iOS. `iOS` `Archived`
- [AppStoreiOS11](https://github.com/aliumujib/AppStoreiOS11) - iOS 11 Appstore clone.. practise of laying out views purely programatically.
- [CarbonKitSwift](https://github.com/melieskubrick/CarbonKitSwift) - CarbonKit is an OpenSource iOS library that includes powerful and beauty UI controllers.
- [EZSwipeController](https://github.com/Esqarrouth/EZSwipeController) - :point_up_2: UIPageViewController like Snapchat/Tinder/iOS Main Pages
- [Instagram-Feed-View](https://github.com/sagarshirbhate/Instagram-Feed-View) - It is a demo view to show feeds as shown in Instagram.All actions(Like,comment,share,follow,etc..) are managed by blocks.
- [interactiveplayerview](https://github.com/AhmettKeskin/InteractivePlayerView) - Custom iOS music player view.
- [MRArticleViewController](https://github.com/mrigdon-zz/MRArticleViewController) - Easily create UIViewControllers for news articles similar to those in the News app.
- [PictureInPicture](https://github.com/malt03/PictureInPicture)
- [SandboxBrowser](https://github.com/aidevjoe/SandboxBrowser) - A simple iOS sandbox file browser, you can share files through AirDrop.
- [ScrollingStackViewController](https://github.com/justeat/ScrollingStackViewController) - A view controller that uses root views of child view controllers as views in a UIStackView. `Archived`
- [ShelfView-iOS](https://github.com/tdscientist/ShelfView-iOS) - iOS custom view to display books on shelf.
- [SIFloatingCollection_Swift](https://github.com/ProudOfZiggy/SIFloatingCollection_Swift) - SIFloatingCollection is a component that provides logic similar to Apple Music genres selection. `iOS`
- [SJSegmentedViewController](https://github.com/subinspathilettu/SJSegmentedViewController) - SJSegmentedScrollView is a light weight generic controller written in Swift 2.3. Its a simple customizable controller were you can integrate any number of ViewControllers into a segmented controller with a header view controller.
- [StackPageView](https://github.com/noppefoxwolf/StackPageView) - SwipeViewController is a Swift modification of RKSwipeBetweenViewControllers - navigate between pages / ViewControllers.
- [StackViewController](https://github.com/seedco/StackViewController) - A controller that uses a UIStackView and view controller composition to display content in a list.
- [SwipeViewController](https://github.com/fortmarek/SwipeViewController) - SwipeViewController enables you to modify the navigation bar and implement 'Swipe Buttons' that can user switch pages with and also the user can easily see which page he is on.
- [Timeline](https://github.com/edekhayser/Timeline) - Timeline like the Path iOS app.
- [TransitionTreasury](https://github.com/dianqk/TransitionTreasury) - Easier way to push your viewController. `Archived`

### Views

- [AbstractView](https://github.com/nuudles/AbstractView) - A simple UIView subclass that you can use as a background view.
- [AHKBendableView](https://github.com/fastred/AHKBendableView) - UIView subclass that bends its edges when its position change is animated
- [Animated-Voice-Blob](https://github.com/constzz/Animated-Voice-Blob) - Animated Voice Blob made like in Telegram mobile app. `iOS` `UIKit`
- [Avatar](https://github.com/wvabrinskas/Avatar) - Generate random user Avatars for apps.
- [AvatarImageView](https://github.com/ayushn21/AvatarImageView) - AvatarImageView is a UIImageView subclass designed to show a user's profile picture, falling back to their initials when a picture is unavailable. `iOS` `Archived`
- [AZEmptyState](https://github.com/Minitour/AZEmptyState) - A UIControl subclass that makes it easy to create empty states.
- [BatteryView](https://github.com/yonat/BatteryView) - Simple battery shaped UIView.
- [Blurable](https://github.com/FlexMonkey/Blurable) - Apply a Gaussian Blur to any UIView with Swift Protocol Extensions
- [CCMRadarView](https://github.com/cacmartinez/CCMRadarView) - Waves of the radar
- [ClapsView](https://github.com/hemangshah/ClapsView) - Implemented the functionality of Medium.com Claps. `Archived`
- [ColorDebugView](https://github.com/jonhull/ColorDebugView) - Simple NS/UIView which can be used to quickly get a view on the screen when roughing out layouts/animations.
- [ComplimentaryGradientView](https://github.com/gkye/ComplimentaryGradientView) - Create complementary gradients generated from dominant and prominent colors in supplied image. Inspired by Grade.js. `iOS`
- [ContactImageView](https://github.com/gkye/ContactImageView) - UIImageView subclass which generates text as the placeholder for an ImageView, supports IBDesignable and code.
- [DottedLineView](https://github.com/STAR-ZERO/DottedLineView) - Draw horizontal or vertical dotted line for iOS.
- [DropPin](https://github.com/dchakarov/DropPin) - If you ever need to pin something `SwiftUI`
- [Elephant](https://github.com/s2mr/Elephant) - Elegant SVG animation kit for swift. `iOS`
- [EZYGradientView](https://github.com/shashankpali/EZYGradientView) - Create gradients and blur gradients without a single line of code.
- [FAQView](https://github.com/mukeshthawani/FAQView) - An easy to use FAQ view for iOS written in Swift. `iOS`
- [FAShimmerViews](https://github.com/fahidattique55/FAShimmerViews) - Custom Shimmer UI Effects.
- [FloatingView](https://github.com/PersianDevelopers/FloatingView) - Floating View
- [FNReactionsView](https://github.com/fabiosoft/FNReactionsView) - FNReactionsView is a customizable control (based on UIView) to give people a way to show floating emoji like facebook does during live stream, easy way.
- [GDPerformanceView](https://github.com/dani-gavrilov/GDPerformanceView-Swift) - Shows FPS, CPU usage, app and iOS versions above the status bar and report FPS and CPU usage via delegate.
- [GLScratchCard](https://github.com/gokulgovind/GLScratchCard) - scratch card effect.
- [Hexacon](https://github.com/gautier-gdx/Hexacon) - A fancy hexagonal layout for displaying data like your Apple Watch. `Archived`
- [HGRippleRadarView](https://github.com/HamzaGhazouani/HGRippleRadarView) - A beautiful radar view to show nearby items (users, restaurants, ...) with ripple animation, fully customizable.
- [HolyView](https://github.com/Frexas/HolyView) - Custom view with transparent circle hole and title/button subview.
- [InAppViewDebugger](https://github.com/indragiek/InAppViewDebugger) - A UIView debugger (like Reveal or Xcode) that can be embedded in an app for on-device view debugging. `iOS`
- [instantsearch-ios](https://github.com/algolia/instantsearch-ios) - A library of widgets and helpers to build instant-search applications on iOS. `iOS`
- [iOSAlignmentIndicatorViews](https://github.com/gbmiranda/iOSAlignmentIndicatorViews) - This is an iOS component to assist in aligning Views by creating lines similar to image editing programs such as Photoshop and Sketch. `iOS`
- [JDMechanicWatch](https://github.com/jamesdouble/JDMechanicWatch) - JDMechanicWatch can show time in a MechanicWatch look.
- [Kingfisher](https://github.com/onevcat/Kingfisher) - Kingfisher is a lightweight and pure Swift implemented library for downloading and caching image from the web. `iOS` `macOS`
- [KRTournamentView](https://github.com/krimpedance/KRTournamentView) - KRTournamentView is a flexible tournament bracket that can respond to the various structure on iOS.
- [LuckyWheel](https://github.com/AhmedNasserSh/iOSLuckyWheel)
- [MacControlCenterUI](https://github.com/orchetect/MacControlCenterUI) - A suite of SwiftUI views that mimic the look and feel of controls used in macOS Control Center (introduced in Big Sur). `macOS` `SwiftUI`
- [MDGroupAvatarView](https://github.com/ttmdung203/MDGroupAvatarView) - This library provides a custom UIView with support for showing group of avatars. It’s used for group chat. The images list can be loaded from local or web url.
- [MPParallaxView](https://github.com/DroidsOnRoids/MPParallaxView) - Apple TV Parallax effect in Swift. `iOS`
- [NightView](https://github.com/Boris-Em/NightView) - Dazzling Nights on iOS.
- [OnlyPictures](https://github.com/KiranJasvanee/OnlyPictures) - A source of circular pictures, currently supports horizontal overlapping or separate pictures with great layout flexibility.
- [OTResizableView](https://github.com/Frog-Frog/OTResizableView) - OTResizableView is a UIView library that can be resized with fingers. `iOS`
- [PartitionKit](https://github.com/kieranb662/PartitionKit) - A SwiftUI Library for creating resizable partitions for View Content. `SwiftUI`
- [peekpop](https://github.com/marmelroy/PeekPop) - Peek and Pop with backwards-compatibility.
- [PIPWKit](https://github.com/nexor-it/PIPWKit) - Picture in Picture Window for iOS.
- [PKHUD](https://github.com/pkluz/PKHUD) - A Swift based reimplementation of the Apple HUD (Volume, Ringer, Rotation,…) for iOS 8.
- [PVView](https://github.com/toannt/PVView) - A small library that helps you to make an amazing parallax view.
- [RoundCode](https://github.com/aslanyanhaik/RoundCode) - RoundCode is a Facebook messenger like custom QR code with lots of customization. `iOS`
- [Shimmer](https://github.com/facebookarchive/Shimmer) - An easy way to add a simple, shimmering effect to any view in an iOS app. `Archived`
- [shiny](https://github.com/maustinstar/shiny) - Add motion-based texture to your SwiftUI views. `iOS` `SwiftUI`
- [Shuffle](https://github.com/mac-gallagher/Shuffle) - A multi-directional card swiping library inspired by Tinder.
- [SingleLineShakeAnimation](https://github.com/haaakon/SingleLineShakeAnimation) - Shake a view with a single line of code with a non-intrusive extension for UIView, with good support for accessability, written in Swift.
- [Skeleton](https://github.com/gonzalonunez/Skeleton) - An easy way to create sliding CAGradientLayer animations! Works great for creating skeleton screens for loading content. `iOS`
- [SkeletonUI](https://github.com/CSolanaM/SkeletonUI) -  Elegant skeleton loading animation in SwiftUI and Combine. `iOS` `macOS` `tvOS` `watchOS` `SwiftUI`
- [SkeletonView](https://github.com/Juanpe/SkeletonView) - An elegant way to show users that something is happening and also prepare them to which contents he is waiting. `iOS`
- [SlidingNumberView](https://github.com/bupstan/SlidingNumberView) - A custom view for animating though initial number and final number with sliding animation. `Archived`
- [Smile-Lock](https://github.com/recruit-lifestyle/Smile-Lock) - A library for make a beautiful Passcode Lock View.
- [SSHoneyCombView](https://github.com/SamehSalama/SSHoneyCombView) - A honey comb View that looks like a collection view with hexagon shaped items.
- [StatusProvider](https://github.com/mariohahn/StatusProvider) - Protocol to handle initial Loadings, Empty Views and Error Handling in a ViewController & views.
- [Stripes](https://github.com/eneko/Stripes) - Beautiful background pattern views for SwiftUI. `SwiftUI`
- [SwiftTickerView](https://github.com/EMart86/SwiftTickerView) - A news ticker view written entirely in swift.
- [SwimplyPlayIndicator](https://github.com/obrhoff/SwimplyPlayIndicator) - Animated PlayIndicator written in SwiftUI. Inspired by Apple's Music Player. `SwiftUI`
- [TB_CustomUIElement](https://github.com/ariok/TB_CustomUIElement) - Implementing custom UI elements with IBDesignable. Enjoy the full
- [Translucid](https://github.com/Ekhoo/Translucid) - Lightweight library to set an Image as text background. Written in swift.
- [Triangulation](https://github.com/younatics/Triangulation) - Triangulation effect in iOS.
- [TvOSPinKeyboard](https://github.com/zattoo/TvOSPinKeyboard) - PIN keyboard for tvOS. `tvOS`
- [Twinkle](https://github.com/piemonte/Twinkle) - Twinkle is a Swift and easy way to make any UIView in your iOS app twinkle. `iOS` `tvOS`
- [TZSpeedometer](https://github.com/tahseen0amin/TZSpeedometer)
- [UIView-Borders-Swift](https://github.com/aaronn/UIView-Borders-Swift) - One sided borders on any side of a UIView. Now available in Swift 3.
- [URWeatherView](https://github.com/Urtaq/URWeatherView) - Show the weather effects onto view written in Swift3.
- [VBPiledView](https://github.com/v-braun/VBPiledView) - Simple and beautiful stacked UIView to use as a replacement for an UITableView, UIImageView or as a menu. `iOS`
- [VCReorderableStackView](https://github.com/avreolko/VCReorderableStackView) - A simple implementation of the drag-and-drop stack view. `iOS`
- [VHUD](https://github.com/xxxAIRINxxx/VHUD) - Simple HUD.
- [VideoThumbnailViewKit](https://github.com/svhawks/VideoThumbnailViewKit) - Video Thumb ScrollView
- [Viewer](https://github.com/3lvis/Viewer) - Image viewer (or Lightbox) with support for local and remote videos and images. `iOS` `Archived`
- [Windless](https://github.com/ParkGwangBeom/Windless) - Windless makes it easy to implement invisible (skeleton) layout loading view. `iOS`
- [Workaholic](https://github.com/hemangshah/Workaholic) - A Github's like work contribution timeline. `Archived`
- [WOWRibbonView](https://github.com/zhouhao27/WOWRibbonView) - Ribbon view for iOS in Swift 3.
- [YGPulseView](https://github.com/YGeorge/YGPulseView) - Pulsing animation for UIView.

## Controls and input

### Badges

- [BadgeHub](https://github.com/jogendra/BadgeHub) - A way to quickly add a notification badge icon to any view. Make any UIView a full fledged animated notification center. `iOS`
- [DNFlyingBadge](https://github.com/normand1/DNFlyingBadge) - DNFlyingBadge is an easy to use and fun control for quick contextual user notification

### Buttons

- [AHDownloadButton](https://github.com/amerhukic/AHDownloadButton) - AHDownloadButton is a customizable download button similar to the download button in the latest version of Apple's App Store app (since iOS 11). `iOS`
- [AMChoice](https://github.com/Abedalkareem/AMChoice) - Radio Button and check box for iOS. `iOS`
- [Animatable](https://github.com/c-villain/Animatable) - Yet another animation modifiers for buttons on pure SwiftUI. `iOS` `SwiftUI`
- [ANLongTapButton](https://github.com/antrix1989/ANLongTapButton) - Long tap button with animated progress bar.
- [ButtonProgressBar-iO](https://github.com/thePsguy/ButtonProgressBar-iOS) - A small and flexible (well documented) UIButton subclass with animated loading progress, and completion animation.
- [ButtonSelectionAnimation](https://github.com/tungfam/ButtonSelectionAnimation) - UIButton subclass which performs animation on selection.
- [ButtonStyleKit](https://github.com/keygx/ButtonStyleKit) - ButtonStyleKit is helper library for UIButton custom styles. `iOS`
- [CRNetworkButton](https://github.com/Cleveroad/CRNetworkButton) - Send Bu#tton for iOS.
- [DOFavoriteButton](https://github.com/okmr-d/DOFavoriteButton) - Cute Animated Button written in Swift.
- [DynamicButton](https://github.com/yannickl/DynamicButton) - Yet another animated flat buttons in Swift
- [EMTNeumorphicView](https://github.com/hirokimu/EMTNeumorphicView) - UIKit views with Neumorphism style design. `UIKit`
- [FacebookLikeReaction](https://github.com/11Shraddha/FacebookLikeReaction) - FacebookLikeReaction is a customizable view which provides more options to share your reactions on any post like Facebook Reactions.
- [fave-button](https://github.com/janselv/fave-button) - FaveButton is an iOS cute animated like button written in Swift.
- [FlatButton](https://github.com/OskarGroth/FlatButton) - Layer based NSButton with Interface Builder styling options. `macOS`
- [GNTickerButton](https://github.com/gonzalonunez/GNTickerButton) - ⏱ Inspired by the Layout app by Instagram, this is a UIButton subclass with a ticker that spins around as desired `Archived`
- [Hamburger Menu Button](https://github.com/toannt/Hamburger-Menu-Button) - Hamburger Menu Button
- [HapticButton](https://github.com/BalestraPatrick/HapticButton) - A button that is triggered based on the 3D Touch pressure, similar to the iOS 11 control center.
- [iOS-camera-button](https://github.com/otusweb/iOS-camera-button) - A button that behave the same way as the video camera button in the iOS camera. `Archived`
- [JDJellyButton](https://github.com/jamesdouble/JDJellyButton) - JDJellyButton is a high-cutomization navigation Button.
- [KDPulseButton](https://github.com/KaiqueDamato/KDPulseButton) - A Custom button that pulses.
- [KSFacebookButton](https://github.com/LeeKahSeng/KSFacebookButton) - Customizable button which look exactly the same as FBSDKLoginButton.
- [KYShutterButton](https://github.com/ykyouhei/KYShutterButton) - KYShutterButton is a custom button that is similar to the shutter button of the camera app `iOS`
- [LGButton](https://github.com/loregr/LGButton) - A fully customisable subclass of the native UIControl which allows you to create beautiful buttons without writing any line of code. `iOS`
- [LiquidFloatingActionButton](https://github.com/yoavlt/LiquidFloatingActionButton) - Material Design Floating Action Button in liquid state
- [loading-buttons-ios](https://github.com/twho/loading-buttons-ios) - A collection of loading buttons and their stylings written in Swift. `iOS`
- [LoadingButton](https://github.com/SeptiyanAndika/LoadingButton) - UIButton subclass with an activity indicator and loading text.
- [LoadingButton](https://github.com/byunkyungmin/LoadingButton) - Simple Loading Animation Button for SwiftUI. `SwiftUI`
- [LTHRadioButton](https://github.com/rolandleth/LTHRadioButton) - A radio button with a pretty animation.
- [MaterialView](https://github.com/karticodes/MaterialView) - Material Floating Button for iOS.
- [MKRingProgressView](https://github.com/maxkonovalov/MKRingProgressView) - Ring progress view similar to Activity app on Apple Watch. `iOS`
- [MMLoadingButton](https://github.com/MillmanY/MMLoadingButton) - Custom Loading Button With Animation.
- [neumorphic-style](https://github.com/hallee/neumorphic-style) - Simple SwiftUI ‘neumorphic’ button style. `SwiftUI`
- [Newly](https://github.com/dhirajjadhao/Newly) - Newly is a drop in solution to add Twitter/Facebook/Linkedin style, new updates/tweets/posts available button. It can be used to notify user about new content availability and can other actions can be triggers using its delegate method.
- [NFFlatButton](https://github.com/norfred/NFFlatButton) - Custom flat button 'à la Letterpress' written in Swift.
- [NKButton](https://github.com/kennic/NKButton) - A fully customizable UIButton.
- [NPFlipButton](https://github.com/neopixl/NPFlipButton)
- [OnOffButton](https://github.com/rakaramos/OnOffButton) - Custom On/Off Animated UIButton, written in Swift.
- [PlayPauseAnimation](https://github.com/kn-neeraj/PlayPauseAnimation) - PlayPause animation based on MIchael villar's motions experiments - http://www.michaelvillar.com/motion
- [PulseAnimation](https://github.com/paritoshraval100/PulseAnimation) - Pulse Button Animation with SwiftUI. `iOS` `SwiftUI`
- [QuickRippleButton](https://github.com/ansonyao/QuickRippleButton) - Custom UIButton which has ripple animation effect when clicked.
- [RadioGroup](https://github.com/yonat/RadioGroup) - The missing iOS radio buttons group.
- [ReactionButton](https://github.com/lojals/ReactionButton) - Since Facebook introduced reactions in 2016, it became a standard in several applications as a way for users to interact with content. ReactionButton is a control that allows developers to add this functionality to their apps in an easy way. `UIKit`
- [Reactions](https://github.com/yannickl/Reactions) - Fully customizable Facebook reactions control.
- [recordbutton](https://github.com/samuelbeek/RecordButton) - A record button in Swift
- [RecordButton](https://github.com/pablogsIO/RecordButton) - A simple iOS record button. `iOS`
- [RNLoadingButton](https://github.com/souzainf3/RNLoadingButton-Swift) - An easy-to-use UIButton subclass with an activity indicator
- [SFlatButton](https://github.com/alexmeji/SFlatButton) - Create a Buttons in Swift like Bootstrap 3.0
- [SparkButtonDemo](https://github.com/saru2020/SparkButtonDemo) - Demonstrates the SparkButton Animations that reflects the FB's Paper App's Like button animation.
- [SquishButton](https://github.com/BalestraPatrick/SquishButton) - A button that squishes when pressed. As seen in the Clips app. `UIKit`
- [SSSpinnerButton](https://github.com/SimformSolutionsPvtLtd/SSSpinnerButton) - Forget about typical stereotypic loading, It's time to change. SSSpinnerButton is an elegant button with a diffrent spinner animations.
- [TKAnimatedCheckButton](https://github.com/takuoka/TKAnimatedCheckButton) - Animated Check Button inspired by http://robb.is/working-on/a-hamburger-button-transition/ and https://dribbble.com/shots/1631598-On-Off
- [TKSubmitTransition](https://github.com/takuoka/TKSubmitTransition) - Animated UIButton of Loading Animation and Transition Animation. Inspired by https://dribbble.com/shots/1945593-Login-Home-Screen
- [TransitionButton](https://github.com/AladinWay/TransitionButton) - UIButton sublass for loading and transition animation. `iOS`
- [TVButton](https://github.com/marmelroy/TVButton) - Recreating the cool parallax icons from Apple TV as iOS UIButtons (in Swift).
- [vkexpandablebutton](https://github.com/vladislav-k/VKExpandableButton) - Easy to use expandable button in Swift.
- [WCLShineButton](https://github.com/imwcl/WCLShineButton) - This is a UI lib for iOS. Effects like shining.
- [WSVideoRecordButton](https://github.com/WebsoftProfession/WSVideoRecordButton) - This is a animatable video record button, easy to integrate Simply set the custom class to your button and use.

### Checkboxes and switches

- [AnimatedSwitch](https://github.com/alsedi/AnimatedSwitch) - Swift subclass of the UISwitch which paints over the parent view with the color if switch is turned on and returns original superview background color if switch is off.
- [CCheckbox-iOS](https://github.com/msalah1193/CCheckbox-iOS) - CCheckbox is a custom UIView which represents custom checkbox component with custom images. `iOS`
- [Custom-Switch](https://github.com/ChadTimmerman/Custom-Switch) - A custom Switch created with UIViews and UIButtons in Swift.
- [MJMaterialSwitch](https://github.com/JaleelNazir/MJMaterialSwitch) - Android Switch button for iOS. `iOS`
- [OGSwitch](https://github.com/OskarGroth/OGSwitch) - iOS-inspired Switch Control for macOS. `macOS`
- [PWSwitch](https://github.com/Shaninnik/PWSwitch) - Highly customizable UISwitch built with CALayers and CAAnimations.
- [SnapchatCheckbox](https://github.com/danielinoa/SnapchatCheckbox) - A Snapchat-inspired checkbox.
- [Switch](https://github.com/T-Pham/Switch) - An iOS switch control implemented in Swift with full Interface Builder support. `iOS`
- [Switcher](https://github.com/knn90/Switcher) - Custom UISwitcher with animation.
- [TKSwitcherCollection](https://github.com/tbxark/TKSwitcherCollection) - An animate switch collection. `iOS` `UIKit`
- [VKCheckbox](https://github.com/vladislav-k/VKCheckbox) - Simple customizable closure-based checkbox control written on Swift.
- [WOWCheckbox](https://github.com/zhouhao27/WOWCheckbox) - Highly customisable checkbox in Swift.

### Contacts pickers

- [EPContactsPicker](https://github.com/ipraba/EPContactsPicker) - A contacts picker component for iOS.
- [EVContactsPicker](https://github.com/edwardvalentini/EVContactsPicker) - Contacts Picker for iOS 9+ that uses the newer Contacts API.

### Controls

- [AGCircularPicker](https://github.com/agilie/AGCircularPicker) - AGCircularPicker is helpful component for creating a controller aimed to manage any calculated parameter.
- [AGVolumeControlView](https://github.com/agilie/AGVolumeControlView) - Visual regulator can be connected to a player or other smart house’s device making the process of controlling the level of a particular characteristic.
- [CircleControl](https://github.com/ChristianMoler/CircleControl)
- [Counter](https://github.com/Juanpe/Counter) - Counter is powerful and multipurpose counter. `iOS`
- [CrownControl](https://github.com/huri000/CrownControl) - CrownControl is a tiny accessory that makes scrolling through scrollable content possible without lifting your thumb. `iOS`
- [padcontrol](https://github.com/gabrieloc/PadControl) - A UIControl subclass for two-dimension directional input.
- [RulerControl](https://github.com/philmitchell/RulerControl) - RulerControl is a draggable, resizable UIControl that provides real world length measurement.
- [SlidingRuler](https://github.com/Pyroh/SlidingRuler) - SlidingRuler is a Swift package containing a SwiftUI control that acts like an linear infinite slider or a finite. `SwiftUI`
- [SpinWheelControl](https://github.com/joshdhenry/SpinWheelControl) - An inertial spinning wheel UI control that allows selection of an item. Cocoapod written in Swift.
- [VolumeControlView](https://github.com/agilie/VolumeControlView) - Visual regulator can be connected to a player or other smart house’s device making the process of controlling the level of a particular characteristic much easier.
- [Wheel-Controller](https://github.com/saurabhsindhu/Wheel-Controller) - Wheel-Controller with a hole.

### Dates and calendars

- [ADDatePicker](https://github.com/abhi-dave/ADDatePicker) - A fully customizable iOS Horizontal PickerView library, written in pure swift.
- [ASCalendar](https://github.com/Aku-n06/ASCalendar) - A calendar control for iOS written in swift with mvvm pattern.
- [CalendarKit](https://github.com/richardtop/CalendarKit) - CalendarKit is a fully customizable calendar library written in Swift. `iOS` `macOS`
- [CalendarPopUp](https://github.com/orazz/CalendarPopUp) - CalendarPopUp - JTAppleCalendar library
- [CalendarView](https://github.com/mmick66/CalendarView) - This is a calendar component for iOS written in Swift.
- [CrispyCalendar](https://github.com/CleverPumpkin/CrispyCalendar)
- [CVCalendar](https://github.com/CVCalendar/CVCalendar) - A custom visual calendar for iOS 8+ written in Swift (>= 4.0). `iOS`
- [D2PDatePicker](https://github.com/di2pra/D2PDatePicker) - Elegant and Easy-to-Use iOS Swift Date Picker. `iOS`
- [DateRangePicker](https://github.com/Timing-GmbH/DateRangePicker) - Date range picker control for OSX. `macOS` `AppKit`
- [DateScrollPicker](https://github.com/alberdev/DateScrollPicker) - Fully customizable date scroll view with picker feature for iOS written in Swift 5.
- [DateTimePicker](https://github.com/itsmeichigo/DateTimePicker) - A nicer iOS UI component for picking date and time.
- [DPTimePicker](https://github.com/dariopellegrini/DPTimePicker) - Custom fullscreen time picker with scrollviews and animations written in Swift.
- [ElegantCalendar](https://github.com/ThasianX/ElegantCalendar) - ElegantCalendar is an efficient and customizable full screen calendar written in SwiftUI. `SwiftUI`
- [EPCalendarPicker](https://github.com/ipraba/EPCalendarPicker) - Colourful calendar for iOS written in Swift.
- [holidaycalendar](https://github.com/ryanmcgrath/holidaycalendar) - This is a demo project of a Holiday (often known as an Advent calendar). `macOS`
- [HorizonCalendar](https://github.com/airbnb/HorizonCalendar) - A declarative, performant, calendar UI component that supports use cases ranging from simple date pickers all the way up to fully-featured calendar apps.
- [ISTimeline](https://github.com/instant-solutions/ISTimeline) - Simple timeline view written in Swift 2.2.
- [JBCalendarDatePicker](https://github.com/joshbirnholz/JBCalendarDatePicker) - A replacement for UIDatePicker made for Catalyst.
- [JTAppleCalendar](https://github.com/patchthecode/JTAppleCalendar) - The final Apple calendar you will ever try. Built for iOS in Swift. `iOS`
- [Koyomi](https://github.com/shoheiyokoyama/Koyomi) - Koyomi is a simple calendar view framework for iOS, written in Swift. `iOS` `Archived`
- [KVKCalendar](https://github.com/kvyatkovskys/KVKCalendar) - A most fully customization calendar library. `iOS`
- [PopOverDatePicker](https://github.com/tichise/PopOverDatePicker) - PopOverDatePicker is a PopOver style DatePicker view. `iOS` `watchOS`
- [RKCalendar](https://github.com/RaffiKian/RKCalendar) - SwiftUI Simple Calendar / Date Picker for iOS. `iOS` `SwiftUI`
- [sambag](https://github.com/mownier/sambag) - Android Time, Month-Year, and Date pickers implemented in Swift for iOS development. `iOS`
- [SCPopDatePicker](https://github.com/scrainie/SCPopDatePicker)
- [ScrollableDatepicker](https://github.com/noxt/ScrollableDatepicker) - Yet another datepicker for iOS.
- [Swift-Calendar](https://github.com/samirpdl/Swift-Calendar) - A swift calendar `iOS`
- [TKCalendarView](https://github.com/powhu/TKCalendarView) - The page curl animation calendar.
- [VNOfficeHourPicker](https://github.com/varun-naharia/VNOfficeHourPicker)
- [WRCalendarView](https://github.com/wayfinders/WRCalendarView) - Calendar Day and Week View for iOS. `iOS`
- [YMCalendar](https://github.com/matsune/YMCalendar) - Monthly event calendar framework for iOS. `iOS`

### Gestures

- [AASignatureView](https://github.com/EngrAhsanAli/AASignatureView) - AASignatureView is a UIView to capture digital signature by drawing it on screen easily in iOS, written in Swift.
- [CTSlidingUpPanel](https://github.com/andriadze/CTSlidingUpPanel) - Transforms any view to sliding panel. `iOS`
- [DBPathRecognizer](https://github.com/didierbrun/DBPathRecognizer) - Gesture recognizer tool [Swift / iOS].
- [Drawsana](https://github.com/Asana/Drawsana) - An open source library that lets your users draw on things - mark up images with text, shapes, etc. `iOS`
- [EPSignature](https://github.com/ipraba/EPSignature) - Signature component for iOS in Swift.
- [GestureLockView](https://github.com/778477/GestureLockView) - User Gesture lock & unlock View. `iOS`
- [InceptionTouch](https://github.com/richzertuche/InceptionTouch) - Who needs 3DTouch when you can have InceptionTouch.
- [Knock](https://github.com/Headtalk/Knock) - A simple detector for physical knocks on the back or front of an iPhone.
- [liquid-swipe](https://github.com/Cuberto/liquid-swipe)
- [NXDrawKit](https://github.com/Nicejinux/NXDrawKit) - NXDrawKit is a simple and easy but useful drawing kit for iPhone.
- [PanSlip](https://github.com/k-lpmg/PanSlip) - Use PanGesture to dismiss view on UIViewController and UIView.
- [PennyPincher](https://github.com/fe9lix/PennyPincher) - A fast gesture recognizer based on the PennyPincher algorithm, written in Swift.
- [RPModalGestureTransition](https://github.com/naoyashiga/RPModalGestureTransition) - You can dismiss modal by using gesture :point_up_2: :iphone:
- [Sensitive](https://github.com/simplisticated/Sensitive) - Fresh look at work with gestures in Swift.
- [sensor-visualizer-kit](https://github.com/asafkorem/sensor-visualizer-kit) - Visualize iOS sensors for live presentations, iOS AppStore demos, Apple Store prototypes, design reviews. `iOS`
- [ShakeToChange](https://github.com/freeskys/ShakeToChange) - Change environment using shake.
- [SHFSignature](https://github.com/felipesantolim/SHFSignature) - It's a simple class that provide to draw a signature and result in UIImage.
- [ShowTime](https://github.com/KaneCheshire/ShowTime) - The easiest way to show off your iOS taps and gestures for demos and videos. `iOS`
- [Signature-Capture](https://github.com/vigneshuvi/iOS-Signature-Capture) - iOS-Signature-Capture is helps to capture the user signature with name and signed date in iOS and supports both Objective-c and Swift languages.
- [SRScratchView](https://github.com/shamshiranees/SRScratchView) - A mask imageView class which can be used a scratchView.
- [Standard-Template-Protocols](https://github.com/cconeil/Standard-Template-Protocols) - Protocols for your every day iOS needs.
- [Tactile](https://github.com/delba/Tactile) - The Swift way to add UIGestureRecognizer and to react to UIControlEvents.
- [TouchesWindow](https://github.com/dmoroz0v/TouchesWindow) - Show touch and force-touch indicators for your iOS app. Have swift and obj-c versions.
- [UndoGesture](https://github.com/procreate/UndoGesture) - This is an example of Procreate's Undo and Redo gestures.
- [WatchShaker](https://github.com/ezefranca/WatchShaker) - Simple motion detector for watchOS shake gesture. `watchOS`

### Keyboards

- [CalculatorKeyboard](https://github.com/sprint84/CalculatorKeyboard) - Custom Input View that mimics a calculator keyboard for fast number input
- [CustomKeyboardTextField](https://github.com/giginet/CustomKeyboardTextField) - Provides easy way to make type safety TextField with custom keyboards.
- [HexadecimalKeyboard](https://github.com/PepperoniJoe/HexadecimalKeyboard) - A native iOS app creating a custom hexadecimal keyboard. `iOS`
- [KBKit](https://github.com/edekhayser/KBKit) - Classes to extend UIKit navigation using key commands. `UIKit`
- [KeyboardAvoidance](https://github.com/radu-costea/KeyboardAvoidance) - Keyboard avoiding kit. The minimal setup you need to make sure that your app can handle easily the appearence / dismissal of the keyboard.
- [KeyboardGuide](https://github.com/niw/KeyboardGuide) - A modern, real iOS keyboard system notifications handler framework that Just Works. `iOS` `UIKit`
- [KeyboardKit](https://github.com/KeyboardKit/KeyboardKit) - KeyboardKit is a Swift library for creating iOS keyboard extension apps. `iOS` `macOS` `tvOS` `watchOS` `visionOS` `SwiftUI`
- [Keyboardy](https://github.com/podkovyrin/Keyboardy) - UIViewController extension for convenient keyboard management. `iOS`
- [KUIKeyboard](https://github.com/Kofktu/KUIKeyboard) - Keyboard Handler in iOS. `iOS`
- [PANumberKeyboard](https://github.com/AlexeyYuPopkov/PANumberKeyboard) - Custom Decimal Number Keyboard.
- [Ribbon](https://github.com/chriszielinski/Ribbon) - A simple cross-platform toolbar/custom input accessory view library for iOS & macOS. `iOS` `macOS`
- [TKKeyboardControl](https://github.com/cokaholic/TKKeyboardControl) - TKKeyboardControl adds keyboard awareness and scrolling dismissal (like iMessages app) to any view with only 1 line of code for Swift.
- [Typist](https://github.com/totocaster/Typist) - Small Swift UIKit keyboard manager for iOS apps. `UIKit`

### Pickers

- [DimensionsPickerView](https://github.com/hussc/DimensionsPickerView)
- [DPPickerManager](https://github.com/priore/DPPickerManager) - UIPicker inside a UIAlertController.
- [DTPhotoViewerController](https://github.com/tungvoduc/DTPhotoViewerController) - A fully customizable photo viewer ViewController to display single photo or collection of photos, inspired by Facebook photo viewer.
- [TimeIntervalPicker](https://github.com/ChernyshenkoTaras/TimeIntervalPicker) - UIDatePicker-like picker in .countDownTimer mode with range selection support.
- [TVOSPicker](https://github.com/cemolcay/TVOSPicker) - A sweet horizontal picker view controller for tvOS. `tvOS`

### Ratings

- [FloatRatingView](https://github.com/glenyi/FloatRatingView) - Whole, half or floating point ratings control written in Swift.
- [STRatingControl](https://github.com/shuhrat10/STRatingControl) - STRatingControl is a UI control that represent the star rating control.

### Segmented controls

- [BetterSegmentedControl](https://github.com/gmarm/BetterSegmentedControl) - BetterSegmentedControl is an easy to use, customizable replacement for UISegmentedControl and UISwitch written in Swift. `iOS`
- [DPSegmentedControl](https://github.com/dwipp/DPSegmentedControl) - Segmented control with image and title.
- [NPSegmentedControl](https://github.com/neopixl/NPSegmentedControl) - A segmented control with custom appearance and interactive animations. Written in Swift 3.0.
- [PinterestSegment](https://github.com/tbxark/PinterestSegment) - A Pinterest-like segment control with masking animation.
- [SJFluidSegmentedControl](https://github.com/sasojadrovski/SJFluidSegmentedControl) - A segmented control with custom appearance and interactive animations. Written in Swift 3.0. `iOS`
- [SSYSegmentedControl](https://github.com/jerrykrinock/SSYSegmentedControl) - UISegmentedControl alternative for text titles. Adaptive segment widths, Swift 3.
- [TwicketSegmentedControl](https://github.com/polqf/TwicketSegmentedControl) - Custom UISegmentedControl replacement for iOS, written in Swift.
- [TZSegmentedControl](https://github.com/tahseen0amin/TZSegmentedControl) - A drop-in replacement for UISegmentedControl mimicking the style of the segmented control used in Google Currents and various other Google products.

### Sliders

- [AdvertisingSlider](https://github.com/seroshtanov/AdvertisingSlider)
- [AlphaSlider](https://github.com/DavidBoyes/AlphaSlider) - A visual improvement of UISlider to be used to specify the alpha value of a color.
- [CircularSlider](https://github.com/taglia3/CircularSlider) - A powerful Circular Slider. It's written in Swift, it's 100% IBDesignable and all parameters are IBInspectable.
- [GradientSlider](https://github.com/jonhull/GradientSlider)
- [HGCircularSlider](https://github.com/HamzaGhazouani/HGCircularSlider) - A custom reusable circular slider control for iOS application. `iOS`
- [iOS-Tactile-Slide](https://github.com/daprice/iOS-Tactile-Slider) - UIControl slider that can be dragged from any point within its bounds, similar to those in Control Center and Home.app. `iOS` `UIKit`
- [JCGGColorSlider](https://github.com/jacquesCedric/JCGGColorSlider) - Colorful NSSlider subclass. `macOS`
- [KJCircularSlider](https://github.com/KiranJasvanee/KJCircularSlider) - Slide circularly. Soon more extended version about to come!
- [MBDoubleSliderExample](https://github.com/c-Viorel/MBDoubleSliderExample) - CustomDoubleSlider for macOs written in swift 3.0. `macOS`
- [MTSlideToOpen-SwiftUI](https://github.com/lemanhtien/MTSlideToOpen-SwiftUI) - A simple SlideToUnlock iOS UI component written in SwiftUI. `iOS` `SwiftUI`
- [NHRangeSlider](https://github.com/thehung111/NHRangeSlider) - A custom range slider in Swift. `Archived`
- [PRGRoundSlider](https://github.com/ispiropoulos/PRGRoundSlider) - A fully customizable circular slider.
- [PUGradientSlider](https://github.com/PayalUmraliya/PUGradientSlider) - Custom UISlider with gradient color background.
- [RangeSlider](https://github.com/matthewreagan/RangeSlider) - Simple, clean, and customizable range-based slider control for macOS. `macOS`
- [RRRangeSliderSwiftUI](https://github.com/Rahul-Mayani/RRRangeSliderSwiftUI) - Custom range slider in SwiftUI. `iOS` `SwiftUI`
- [SHSliderSwitch](https://github.com/iamshezad/SHSliderSwitch) - SHSliderSwitch is a simple lightweight library to implement an animated slider switch.
- [SlidableImage](https://github.com/quver/SlidableImage) - Easy to use library for before & after images. One-line initialization and very customizable API.
- [SlideTo](https://github.com/ChristianMoler/SlideTo) - Simple slide controller is fully customizable via interface builder.
- [SnappingSlider](https://github.com/rehatkathuria/SnappingSlider) - A beautiful slider control for iOS built purely upon Swift. `Archived`
- [SpringySlider](https://github.com/josephlord/SpringySlider) - Custom UISlider with thumb animation.
- [SSSlider](https://github.com/ngodacdu/SSSlider) - A customisable Slider which will show a tooltip when dragging the slider.
- [TGPControls](https://github.com/SwiftArchitect/TGPControls) - Drop-in replacement for UISlider with ticks, images & animated labels.
- [TNAnimateSlider](https://github.com/nguyenvantrai2011/TNAnimateSlider) - Custome UISlider with thumb animation
- [TNSlider](https://github.com/tiennth/TNSlider) - A custom iOS slider that show current value on the thumb. `iOS`
- [WESlider](https://github.com/Ekhoo/WESlider) - Simple and light weight slider with chapter management.
- [WOWMarkSlider](https://github.com/zhouhao27/WOWMarkSlider) - A customisable UISlider.

### Steppers

- [AHStepperControl](https://github.com/ashh640/AHStepperControl) - A simple stepper control for iOS.
- [DSFStepperView](https://github.com/dagronf/DSFStepperView) - A custom stepper text field for macOS. `iOS` `macOS` `SwiftUI`
- [G8SliderStep](https://github.com/gali8/G8SliderStep) - Custom Range UISlider for iOS, in Swift - Draggable, Tappable, Inspectable.
- [GMStepper](https://github.com/gmertk/GMStepper) - A stepper with a sliding label in the middle.
- [JKSteppedProgressBar](https://github.com/jkmathew/JKSteppedProgressBar) - Stepped ProgressBar for iOS.
- [KWStepper](https://github.com/kyleweiner/KWStepper) - A stepper control with flexible UI and tailored UX.
- [MultiStepSlider](https://github.com/hsusmita/MultiStepSlider) - A custom UIControl which functions like UISlider where you can set multiple intervals with different step values for each interval.
- [SnappingStepper](https://github.com/yannickl/SnappingStepper) - An elegant alternative to the UIStepper written in Swift.
- [Stepperier](https://github.com/NSDavidObject/Stepperier) - Interactive snapping stepper.
- [StepperView](https://github.com/badrinathvm/StepperView) - SwiftUI iOS component for Step Indications. `iOS` `SwiftUI`
- [StepSlider](https://github.com/spromicky/StepSlider) - StepSlider its custom implementation of slider such as UISlider for preset integer values. `iOS` `UIKit`

### Tags and tokens

- [ARSelectableView](https://github.com/MakwanaRohit/ARSelectableView) - Provide selection type radio, checkbox and tag.
- [automatic-height-tagcells](https://github.com/weijentu/automatic-height-tagcells) - This is a sample project to implement features with dynamic height of UITableViewCell based on autolayout, tags aligned automatically and clickable tags. `iOS`
- [DBSphereTagCloudSwift](https://github.com/apparition47/DBSphereTagCloudSwift) - A 3D spherical tag cloud view for iOS using UIKit and Accelerate. `iOS` `UIKit`
- [DPColorfulTags](https://github.com/HongliYu/DPColorfulTags-Swift) - tags with different colors. `Archived`
- [GravityTagCloudView](https://github.com/billypchan/GravityTagCloudView) - A tag cloud view with gravity.
- [Hashtags](https://github.com/scaraux/Hashtags) - A Swift library to display and manipulate Hashtags as a list.
- [RRTagController](https://github.com/remirobert/RRTagController) - RRTagController allows user to select tag and create new one. `Archived`
- [SSCTaglistView](https://github.com/sanjaysinh-Chauhan/SSCTaglistView) - Customizable iOS tag list view, in Swift.
- [TagListView](https://github.com/ElaWorkshop/TagListView) - Simple but highly customizable iOS tag list view, in Swift. `Archived`
- [UITags](https://github.com/gtsifrikas/UITags)
- [WSTagsField](https://github.com/whitesmith/WSTagsField) - An iOS text field that represents different Tags. `iOS`
- [YNSearch](https://github.com/younatics/YNSearch) -  Awesome fully customize search view like Pinterest written in Swift 3. `iOS`
- [YZTagView](https://github.com/yoshiz3-onishi/YZTagView) - A simple tag view.

### Text fields and forms

- [AnimatedTextInput](https://github.com/jobandtalent/AnimatedTextInput) - Animated UITextField and UITextView replacement for iOS. `Archived`
- [AutocompleteField](https://github.com/filipstefansson/AutocompleteField) - Add word completion to your UITextFields.
- [CHIOTPField](https://github.com/ChiliLabs/CHIOTPField) - CHIOTPField is a set of textfields that can be used for One-time passwords, SMS codes, PIN codes, etc.
- [DateTextField](https://github.com/BeauNouvelle/DateTextField) - A Swift UITextField subclass designed to make entering dates easier, faster and more flexible than the standard UIDatePicker. `iOS`
- [DossyTextLabel](https://github.com/joeynelson42/DossyTextLabel) - A subclass of UILabel reminiscent of Strong Bad's faithful Tandy 400. `iOS` `UIKit`
- [DWAnimatedLabel](https://github.com/Dywane/DWAnimatedLabel) - An UILabel subclass that lets you animate text with different types. `UIKit`
- [EGFloatingTextField](https://github.com/enisgayretli/EGFloatingTextField) - Implementation of Google's "Floating labels" of Material design.
- [ElValidator](https://github.com/dk53/ElValidator) - A simple plugin to help you validate textfield entries.
- [FloatingPromptTextField](https://github.com/EmilioPelaez/FloatingPromptTextField) - A SwiftUI TextField with a prompt (or placeholder) that floats above the text field when active or not empty. Requires iOS 15. `SwiftUI`
- [FloatLabelFields](https://github.com/FahimF/FloatLabelFields) - Text entry controls which contain a built-in title/label so that you don't have to add a separate title for each field.
- [Form](https://github.com/iZettle/Form) - Form is an iOS Swift library for building and styling UIs. `iOS` `Archived`
- [Former](https://github.com/ra1028/Former) - Former is a fully customizable Swift2 library for easy creating UITableView based form.
- [FormToolbar](https://github.com/sgr-ksmt/FormToolbar) - Simple, movable and powerful toolbar for UITextField and UITextView. `iOS`
- [formvalidator-swift](https://github.com/ustwo/formvalidator-swift) - A framework to validate inputs of text fields and text views in a convenient way. `iOS` `macOS` `tvOS`
- [ImageTextField](https://github.com/Sahilberi/ImageTextField) - A Designable Textfield For adding textfield leftview and rightview images in storyboard for swift 3.0.
- [iPhoneNumberField](https://github.com/MojtabaHs/iPhoneNumberField) - Format phone numbers as they're typed—entirely in SwiftUI. `SwiftUI`
- [KAPinField](https://github.com/alexiscreuzot/KAPinField) - Lightweight Pin Code Field library for iOS, written in Swift.
- [LTBouncyPlaceholder](https://github.com/lexrus/LTBouncyPlaceholder) - A learning-by-doing UITextField extension written in Swift `Archived`
- [MMText](https://github.com/MillmanY/MMText) - Text Edit with error and title string.
- [MPGTextField](https://github.com/gwadhwani/MPGTextField) - An autocomplete textfield for iOS which provides suggestions as you type.
- [NSJTextField](https://github.com/NSJoker/NSJTextField) - A custom textfield with the placeholder displayed on top when text entered. `iOS`
- [ParkedTextField](https://github.com/gmertk/ParkedTextField) - A text field with a constant text/placeholder.
- [PasswordTextField](https://github.com/PiXeL16/PasswordTextField) - A custom TextField with a switchable icon which shows or hides the password and enforces good password policies, written in Swift.
- [PinCodeTextField](https://github.com/tkach/PinCodeTextField) - Simple pin code text input with underlined space for characters.
- [PRGValidationField](https://github.com/ispiropoulos/PRGValidationField) - A Better way to make registration forms.
- [RAGTextField](https://github.com/raginmari/RAGTextField) - Subclass of UITextField that adds an animated placeholder and an optional hint label below the text. `iOS`
- [RSFloatInputView](https://github.com/roytornado/RSFloatInputView) - A Float Input View with smooth animation and supporting icon and seperator written with Swift.
- [SelectableTextView](https://github.com/jhurray/SelectableTextView) - A text view that supports selection and expansion.
- [SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField) - A beautiful and flexible text field control implementation of "Float Label Pattern". Written in Swift. As used in the Skyscanner TravelPro iOS app. `Archived`
- [SwiftCop](https://github.com/andresinaka/SwiftCop) - SwiftCop is a validation library fully written in Swift and inspired by the clarity of Ruby On Rails Active Record validations.
- [SwiftForms](https://github.com/ortuman/SwiftForms) - A small and lightweight library written in Swift that allows you to easily create forms. `Archived`
- [SwiftUIFormValidator](https://github.com/MalekKamel/SwiftUIFormValidator) - Declarative form validator for SwiftUI. `SwiftUI`
- [SwiftValidators](https://github.com/gkaimakas/SwiftValidators) - String validation for iOS. `iOS` `Archived`
- [SwiftyFORM](https://github.com/neoneye/SwiftyFORM) - Form framework for iOS written in Swift. `iOS`
- [TextFieldCounter](https://github.com/serralvo/TextFieldCounter) - UITextField character counter with lovable UX.
- [TextFieldEffects](https://github.com/raulriera/TextFieldEffects) - Custom UITextFields effects inspired by Codrops, built using Swift.
- [textfields](https://github.com/alxyzhv/textfields) - Animate placeholders in UITextField `iOS`
- [TKFormTextField](https://github.com/hlung/TKFormTextField) - A nice UITextField subclass with built-in error label, floating label while editing, and underline. `iOS`
- [TLFloatLabelTextField](https://github.com/BhagyashreeMynamwar/TLFloatLabelTextField) - A Beautiful and flexible text field control(along with the bottom line) implementation of "Float Label Pattern".
- [TweeTextField](https://github.com/oleghnidets/TweeTextField) - Lightweight set of text fields with nice animation and functionality. `iOS` `UIKit`
- [UITextField-Navigation](https://github.com/T-Pham/UITextField-Navigation) - UITextField-Navigation make it easier to navigate between UITextFields. `iOS`
- [UnderLineTextField](https://github.com/mohammadalijf/UnderLineTextField) - Simple UITextfield Subclass with state. `iOS`
- [VEditorKit](https://github.com/GeekTree0101/VEditorKit) - Lightweight and Powerful Editor Kit. `iOS`
- [VKAfterTimeTextField](https://github.com/vladislav-k/VKAfterTimeTextField) - VKAfterTimeTextField is a sub-class of UITextField which allows you to know when user edited it last time during current use session. Also it allows to notify after specific time interval when user ends editing. This is gives you a some kind of "setContinouos:false" feature like UISlider has.
- [VMFloatLabel](https://github.com/jimmyjose-dev/VMFloatLabel) - Swift based UITextField subclass with floating labels.

## Lists and scrolling

### Collection views

- [ADMozaicCollectionViewLayout](https://github.com/Antondomashnev/ADMozaicCollectionViewLayout) - ADMozaicCollectionViewLayout is yet another UICollectionViewLayout subclass that implements "brick" or "mozaic" layout.
- [ALBusSeatView](https://github.com/applogistdev/ALBusSeatView) - Bus Seat View Selection.
- [AlignedCollectionViewFlowLayout](https://github.com/mischa-hildebrand/AlignedCollectionViewFlowLayout) - A collection view layout that gives you control over the horizontal and vertical alignment of the cells. `iOS` `UIKit`
- [AnimatedCollectionViewLayout](https://github.com/KelvinJin/AnimatedCollectionViewLayout) - A UICollectionViewLayout subclass that adds custom transitions/animations to the UICollectionView without effecting your existing code. `iOS`
- [appstore-clone](https://github.com/phillfarrugia/appstore-clone) - An experimental clone of the new iOS 11 App Store app.
- [ASCollectionView](https://github.com/apptekstudios/ASCollectionView) - A SwiftUI collection view with support for custom layouts, preloading, and more. `iOS` `SwiftUI` `Archived`
- [AZCollectionView](https://github.com/AfrozZaheer/AZCollectionViewController) - Easy way to integrate pagination with dummy views in CollectionView, make Instagram "Discover" within minutes.
- [BouncyLayout](https://github.com/roberthein/BouncyLayout) - BouncyLayout is a collection view layout that makes your cells bounce.
- [Buffer](https://github.com/alexdrone/Buffer) - Swift μ-framework for efficient array diffs, collection observation and cell configuration. `iOS`
- [CalendarHeatmap](https://github.com/Zacharysp/CalendarHeatmap) - CalendarHeatmap is a calendar based heatmap which presenting a time series of data points in colors, inspired by Github contribution chart, and written in Swift.
- [CarLensCollectionViewLayout](https://github.com/netguru/CarLensCollectionViewLayout) - An easy-to-use Collection View Layout for card-like animation. `iOS` `Archived`
- [CellAnimation](https://github.com/martinslapinskis/CellAnimation) - UICollectionView cell animations with CGAffineTransform
- [ChainPageCollectionView](https://github.com/jindulys/ChainPageCollectionView) - A custom View with two level chained collection views and fancy transition animation. `iOS`
- [Changeset](https://github.com/osteslag/Changeset) - Minimal edits from one collection to another. `iOS` `macOS`
- [CheckmarkCollectionViewCell](https://github.com/yonat/CheckmarkCollectionViewCell) - UICollectionViewCell with checkbox when it isSelected and empty circle when not - like Photos.app "Select" mode.
- [circular-carousel](https://github.com/Ramotion/circular-carousel) - List a collection of items in a horizontally scrolling view. `iOS`
- [CKWaveCollectionViewTransition](https://github.com/CezaryKopacz/CKWaveCollectionViewTransition) - Cool custom transition between two or more UICollectionViewControllers.
- [CollectionKit](https://github.com/SoySauceLab/CollectionKit) - Reimagining UICollectionView. `iOS`
- [CollectionLayouts](https://github.com/Oni-zerone/CollectionLayouts) - This is a UICollectionViewLayout that reproduce the Instagram Stories experience, just use StoriesCollectionViewLayout in your UICollectionView and subclass your cells from StoriesCollectionViewCell!.
- [CollectionViewCustom](https://github.com/damienromito/CollectionViewCustom) - Custom CollectionViewLayout with a custom paging size by overriding scrollViewWillEndDragging.
- [CollectionViewPagingLayout](https://github.com/amirdew/CollectionViewPagingLayout) - Simple layout for make paging with UICollectionView. `SwiftUI` `UIKit` `Archived`
- [CollectionViewShelfLayout](https://github.com/pitiphong-p/CollectionViewShelfLayout) - A UICollectionViewLayout subclass displays its items as rows of items similar to the App Store Feature tab without a nested UITableView/UICollectionView hack.
- [CollectionViewSlantedLayout](https://github.com/yacir/CollectionViewSlantedLayout) - CollectionViewSlantedLayout is a subclass of the UICollectionViewLayout allowing the display of slanted cells in a UICollectionView. `iOS` `UIKit`
- [Compositional-layouts-kit](https://github.com/eleev/compositional-layouts-kit) - A set of advanced compositional layouts for UICollectionView with examples. `iOS` `UIKit`
- [CPCollectionViewKit](https://github.com/ParsifalC/CPCollectionViewKit) - CollectionViewTransitionLayout.
- [DifferenceKit](https://github.com/ra1028/DifferenceKit) - A fast and flexible O(n) difference algorithm framework for Swift collection.
- [Differific](https://github.com/zenangst/Differific) - Differific - a fast and convenient diffing framework.
- [DisplaySwitcher](https://github.com/Yalantis/DisplaySwitcher) - Custom transition between two collection view layouts. `iOS`
- [DragDropCollection](https://github.com/runrunrun/DragDropCollection) - Custom UICollectionView allowing cells to be dragged and dropped.
- [DraggableGridView](https://github.com/fullc0de/DraggableGridView) - A grid style collection view written in SwiftUI that supports to change a position of any item on it by dragging. `SwiftUI`
- [Elliotable](https://github.com/bbdyno/Elliotable) - Elliotable is simple library to generate Timetable of University. `iOS`
- [expandable-collection-view-kit](https://github.com/eleev/expandable-collection-view-kit) - Expandable, hierarchical, flexible, declarative UICollectionView with diffable data sources & SwiftUI-like tree items builder. `iOS` `SwiftUI`
- [FadingEdgesCollectionView](https://github.com/alexandre-g/FadingEdgesCollectionView) - A UICollectionView that fades it's edges to hint about more content.
- [flexiblerowheightgridlayout](https://github.com/rwbutler/FlexibleRowHeightGridLayout) - A UICollectionView grid layout designed to support Dynamic Type by allowing the height of each row to size to fit content.
- [FlowLayout](https://github.com/avdyushin/FlowLayout) - UICollectionViewFlowLayout with alignment modes.
- [FSPagerView](https://github.com/WenchaoD/FSPagerView) - FSPagerView is an elegant Screen Slide Library implemented primarily with UICollectionView. It is extremely helpful for making Banner, Product Show, Welcome/Guide Pages, Screen/ViewController Sliders. `iOS`
- [gliding-collection](https://github.com/Ramotion/gliding-collection) - Gliding Collection is a smooth, flowing, customizable decision for a UICollectionView Swift Controller. `iOS`
- [GooglePlayTransition](https://github.com/xxxAIRINxxx/GooglePlayTransition) - Custom transition like Google Play Store Android App. written in Swift.
- [Hanabi](https://github.com/ivanlisovyi/Hanabi) - UICollectionViewLayout subclass with a focus on UICollectionViewCell content. `Archived`
- [HorizontalStickyHeaderLayout](https://github.com/toshi0383/HorizontalStickyHeaderLayout) - Horizontal UICollectionViewLayout with Sticky HeaderView. `iOS` `tvOS`
- [IBPCollectionViewCompositionalLayout](https://github.com/kishikawakatsumi/IBPCollectionViewCompositionalLayout) - Backport of UICollectionViewCompositionalLayout to earlier iOS 12. `UIKit`
- [InfiniteScrolling](https://github.com/Vishal-Singh-Panwar/InfiniteScrolling) - Add infinite scrolling to collection view.
- [ios-inshorts-view](https://github.com/SwiftCrew/ios-inshorts-view) - InshortsView, UICollectionView for implementing vertical swipe up-done for next/previous cards, like News Inshorts application. `iOS`
- [IOStickyHeader](https://github.com/BenjaminPrieur/IOStickyHeader) - Parallax and Sticky header done right using UICollectionViewLayout.
- [KDDragAndDropCollectionView](https://github.com/mmick66/KDDragAndDropCollectionView) - Dragging and Dropping data across multiple UICollectionViews.
- [KRLCollectionViewGridLayout](https://github.com/JayGajjar/JGTransitionCollectionView/tree/master/JGTransitionCollectionView) - A iOS swift base collectionview with unique animation feature inspired from behance made using UICollectionView.
- [KSImageCarousel](https://github.com/LeeKahSeng/KSImageCarousel) - Lightweight image carousel which can easily adapt to different type of image source.
- [LNZCollectionLayouts](https://github.com/gringoireDM/LNZCollectionLayouts) - A collection of CollectionViewLayout.
- [MagazineLayout](https://github.com/airbnb/MagazineLayout) - A collection view layout capable of laying out views in vertically scrolling grids and lists.
- [MHPinterestLayout](https://github.com/michaelhenry/MHPinterestLayout) - Customized dynamic cell - Pinterest layout with custom header.
- [PinterestLayout](https://github.com/MagicLab-team/PinterestLayout) - Custom collection view layout inspired by Pinterest layout. Written in Swift. `iOS`
- [PopupCollectionViewController](https://github.com/corin8823/PopupCollectionViewController) - PopupCollectionViewController is a collectionView in Popup view.
- [RAMReel](https://github.com/Ramotion/reel-search) - RAMReel is a controller that allows you to choose options from a list. `iOS`
- [RAReorderableLayout](https://github.com/ra1028/RAReorderableLayout) - A UICollectionView layout whitch can move item with drag and drop. `Archived`
- [ReorderableGridView-Swift](https://github.com/cemolcay/ReorderableGridView-Swift) - Reorderable grid view solution implemented with swift.
- [RSKCollectionViewRetractableFirstItemLayout](https://github.com/ruslanskorb/RSKCollectionViewRetractableFirstItemLayout) - A light-weight UICollectionViewFlowLayout subclass that allows the first item to be retractable.
- [SACollectionViewVerticalScalingFlowLayout](https://github.com/marty-suzuki/SACollectionViewVerticalScalingFlowLayout) - UICollectionViewLayout that performs scaling up and down automatically on disappearing cells, and applies UIDynamics. `Archived`
- [Sapporo](https://github.com/nghialv/Sapporo) - Cellmodel-driven collectionview manager.
- [ScaledVisibleCellsCollectionView](https://github.com/ikemai/ScaledVisibleCellsCollectionView) - ScaledVisibleCellsCollectionView is UICollectionView extension. ScaledVisibleCellsCollectionView is Check visible cells position. And setting cell's scale and alpha.
- [ScalingCarousel](https://github.com/aataraxiaa/scalingcarousel) - A super simple carousel view with scaling transitions written in Swift. `iOS` `Archived`
- [SectionScrubber](https://github.com/3lvis/SectionScrubber) - A component to quickly scroll between collection view sections. `Archived`
- [SimpleCollectionViewBooking](https://github.com/theedov/SimpleCollectionViewBooking) - A simple booking feature using CollectionView and Compositional Layout. Available dates for booking come form a simple API. `iOS`
- [smooth-scroll](https://github.com/Cuberto/smooth-scroll) - Smooth collection scrolling.
- [SnapLikeCollectionView](https://github.com/kboy-silvergym/SnapLikeCollectionView) - The collectionView library which is scaling, scrolling and stopping comfortably like Snapchat and Instagram.
- [SNCollectionViewLayout](https://github.com/ahmedAlmasri/SNCollectionViewLayout) - Collection View Layouts is a set of custom flow layouts for iOS which imitate general data grid approaches for mobile apps. `iOS`
- [SquareFlowLayout](https://github.com/ChernyshenkoTaras/SquareFlowLayout) - SquareFlowLayout is another UICollectionViewLayout subclass that implements Instagram style layout.
- [StackedCollectionView](https://github.com/oakstudios/StackedCollectionView) - Swift library to drag, drop, and stack items within a UICollectionView.
- [StickyCollectionView](https://github.com/matbeich/StickyCollectionView) - UICollectionView layout for presenting of the overlapping cells.
- [StickyLayout](https://github.com/jeffreysfllo24/StickyLayout) - Sticky Layout for UICollectionViews!
- [SwiftSpreadsheet](https://github.com/stuffrabbit/SwiftSpreadsheet) - Spreadsheet CollectionViewLayout in Swift. Fully customizable.
- [SwiftyCollectionView](https://github.com/vinit5320/SwiftyCollectionView) - [Tutorial](https://swiftyos.wordpress.com/2015/08/01/animated-wave-transition-collectionview-ckwavecollectionviewtransition/)
- [swipeable-view-stack](https://github.com/phillfarrugia/swipeable-view-stack) - A Swipeable Stack of Views similar to a popular dating app but for swiping through anything.
- [SwipeCollectionViewCell](https://github.com/anishparajuli555/SwipeCollectionViewCell) - This project illustrates how to implement swipe to delete functionality in UICollectionViewCell.
- [TabbedCollectionView](https://github.com/sprint84/TabbedCollectionView) - Multi-page collection view with tab categories.
- [ugrid](https://github.com/AramSemerjyan/ugrid) - Custom grid view based on UICollectionView and Swift `iOS`
- [UICollectionViewAnimatedTransition](https://github.com/spromicky/UICollectionViewAnimatedTransition) - Implementation for some kind of "folder to content" animation for UICollectionView. `iOS` `UIKit`
- [UPCarouselFlowLayout](https://github.com/zepojo/UPCarouselFlowLayout) - A fancy carousel flow layout for UICollectionView on iOS.
- [VegaScroll](https://github.com/ApplikeySolutions/VegaScroll) - VegaScroll is a lightweight animation flowlayout for UICollectionView completely written in Swift 4, compatible with iOS 11 and Xcode 9. `iOS`
- [WatchLayout](https://github.com/HocTran/WatchLayout) - A simple bubble watch-like layout for UICollectionView
- [ZLBalancedFlowLayout](https://github.com/zhxnlai/ZLBalancedFlowLayout) - A UICollectionViewFlowLayout subclass that scales items to take up space, optimized for large item set.

### Pull to refresh

- [AARefreshControl](https://github.com/EngrAhsanAli/AARefreshControl) - AARefreshControl is a pull to refresh control for UITableVIew and UICollectionView.
- [ADChromePullToRefresh](https://github.com/Antondomashnev/ADChromePullToRefresh) - ADChromePullToRefresh
- [AMRefresher](https://github.com/arturdev/AMRefresher) - Super easy way to use "Pull To Refresh" and "Infinite Scrolling" with 1 line of code. `iOS` `Archived`
- [DGElasticPullToRefresh](https://github.com/gontovnik/DGElasticPullToRefresh) - Elastic pull to refresh compontent developed in Swift.
- [FlippingNotch](https://github.com/QuickBirdEng/FlippingNotch) - Flipping Notch.
- [GearRefreshControl](https://github.com/andreamazz/GearRefreshControl) - A custom animation for the UIRefreshControl
- [GIFRefreshControl](https://github.com/delannoyk/GIFRefreshControl) - GIFRefreshControl is a pull to refresh that supports GIF images as track animations.
- [JZSpringRefresh](https://github.com/newbdez33/JZSpringRefresh) - All around Unread.app like pull to refresh library.
- [MAGearRefreshControl](https://github.com/micazeve/MAGearRefreshControl) - An iOS refresh control with gear animation `iOS`
- [PeriscopyPullToRefresh](https://github.com/anaglik/PeriscopyPullToRefresh) - Pull-To-Refresh view inspired by Periscope application written in swift `iOS`
- [PullRefresh](https://github.com/zhaokaiyuan99/PullRefresh) - 用swift 写的 Refresh控件 支持继承uiscrollview的控件（uitableview,uicollectionview）
- [PullToBounce](https://github.com/takuoka/PullToBounce) - Animated "Pull To Refresh" Library for UIScrollView. Inspired by https://dribbble.com/shots/1797373-Pull-Down-To-Refresh `iOS`
- [PullToMakeFlight](https://github.com/Yalantis/PullToMakeFlight) - Custom animated pull-to-refresh that can be easily added to UIScrollView `iOS`
- [PullToMakeSoup](https://github.com/Yalantis/PullToMakeSoup) - Custom animated pull-to-refresh that can be easily added to UIScrollView `iOS`
- [PullToReach](https://github.com/QuickBirdEng/PullToReach) - PullToReach is a simple drag-and-drop solution for adding pull-to-reach functionality to your app
- [PullToRefresh](https://github.com/Yalantis/PullToRefresh) - This component implements pure pull-to-refresh logic and you can use it for developing your own pull-to-refresh animations. `iOS`
- [PZPullToRefresh](https://github.com/pixyzehn/PZPullToRefresh) - This is the simplest refresh control in Swift. `Archived`
- [RainyRefreshControl](https://github.com/Onix-Systems/RainyRefreshControl) - Simple refresh control for iOS based on SpriteKit and Core Graphics
- [Refresher](https://github.com/jcavar/refresher) - PullToReach is a simple drag-and-drop solution for adding pull-to-reach functionality to your app.
- [ReplaceAnimation](https://github.com/fruitcoder/ReplaceAnimation) - Implementation of [Zee Young's Dribbble animation](https://dribbble.com/shots/2067564-Replace)
- [SSCustomPullToRefresh](https://github.com/SimformSolutionsPvtLtd/SSCustomPullToRefresh) - SSCustomPullToRefresh is an open-source library that uses UIKit to add an animation to the pull to refresh view in a UITableView and UICollectionView. `iOS` `UIKit`
- [TB_PeriscopePTR](https://github.com/ariok/TB_PeriscopePTR) - tutorial [here](https://www.thinkandbuild.it/implementing-the-periscope-app-pull-to-refresh/)
- [WAPullToShare](https://github.com/wendyabrantes/WAPullToShare) - Mobile Pull to share inspired from Google Chrome refresh / new tab actions.

### Scroll views

- [AppStoreStyleHorizontalScrollView](https://github.com/terenceLuffy/AppStoreStyleHorizontalScrollView) - App store style horizontal scroll view.
- [CMLazyScrollViewController](https://github.com/Mycose/CMLazyScrollViewController) - Lazy ScrollView with support for infinite scroll (using a paging system with UIViewControllers and not UIViews).
- [CrossNavigation](https://github.com/artemstepanenko/CrossNavigation) - Any side navigation.
- [FlexibleHeader](https://github.com/k-lpmg/FlexibleHeader) - A container view that responds to scrolling of UIScrollView. `iOS`
- [Image-Carousel](https://github.com/robertrr61/Image-Carousel) - Add an array of images to a view and scroll them.
- [Infinite-Grid-Swift](https://github.com/freshcode/Infinite-Grid-Swift) - Implementing an infinite grid using UIScrollview on iOS. `iOS` `UIKit`
- [LoopedContentsView](https://github.com/naru-jpn/LoopedContentsView) - View to display looped contents.
- [MXParallaxHeader](https://github.com/maxep/MXParallaxHeader) - Simple parallax header for UIScrollView. `Archived`
- [PagingMenuController](https://github.com/kitasuke/PagingMenuController) - Paging view controller with customizable menu in Swift `Archived`
- [PSFadingScrollView](https://github.com/Vugla/PSFadingScrollView) `iOS`
- [RMShapesPageControl](https://github.com/rupammitra/RMShapesPageControl) - A custom page control having custom shapes as indicators works both vertically and horizontally.
- [ScrollingContentViewController](https://github.com/drewolbrich/ScrollingContentViewController) - ScrollingContentViewController makes it easy to create a view controller with a single scrolling content view, or to `iOS` `UIKit`
- [scrollview-reactive-header](https://github.com/swiftui-library/scrollview-reactive-header) - A replacement ScrollView that provides a header with subtle scroll animations. `SwiftUI`
- [SegementSlide](https://github.com/Jiar/SegementSlide) - Multi-tier UIScrollView nested scrolling solution.
- [TGLParallaxCarousel](https://github.com/taglia3/TGLParallaxCarousel) - A lightweight 3D Linear Carousel with parallax effect
- [ZKCarousel](https://github.com/ZacharyKhan/ZKCarousel) - A simple carousel implementation written in Swift. `iOS`

### Table views

- [AccordionTableViewController](https://github.com/klevison/KMAccordionTableViewController) - Accordion UITableViewController component based on Apples's example.
- [ActionCell](https://github.com/xiongxiong/ActionCell) - Easy to use UITableViewCell implementing swiping to trigger actions (known from the Mailbox App).
- [APSGroupedTableView](https://github.com/AishPratap/APSGroupedTableView)
- [BWSwipeRevealCell](https://github.com/bitwit/BWSwipeRevealCell) - A Swift library for swipeable table cells.
- [CascadingTableDelegate](https://github.com/edopelawi/CascadingTableDelegate) - A no-nonsense way to write cleaner UITableViewDelegate and UITableViewDataSource in Swift. `iOS`
- [CITreeView](https://github.com/cenksk/CITreeView) - CITreeView created to implement and maintain that wanted TreeView structures for IOS platforms easy way.
- [COBezierTableView](https://github.com/knutigro/COBezierTableView) - UITableView modification written in Swift where cells are scrolling in an arc defined by a BezierPath.
- [ConfigurableTableViewController](https://github.com/fastred/ConfigurableTableViewController) - Typed, yet Flexible Table View Controller.
- [elongation-preview](https://github.com/Ramotion/elongation-preview) - ElongationPreview is an elegant push-pop style view controller. `iOS`
- [EssentialTableView](https://github.com/sohamb1390/EssentialTableView) - A detailed project on UITableView which includes Parallax effects, Collapse/Expand UITableViewCell, 3D Touch on UITableViewCell.
- [EVSlidingTableViewCell](https://github.com/epv44/EVSlidingTableViewCell) - Custom UITableViewCell that can be swiped either way to reveal a "drawer" with between 1 and 4 customizable action buttons. These action buttons fade and grow into view as the drawer is swiped. This cell works on all orientations and all devices.
- [ExpandableCell](https://github.com/younatics/ExpandableCell) - Awesome expandable, collapsible tableview cell for iOS written in Swift 4. `iOS`
- [ExpandableTableView](https://github.com/rondinellimorais/ExpandableTableView) - UIExpandableTableView
- [ExpandingStackCells](https://github.com/jozsef-vesza/ExpandingStackCells) - Expanding table view cells using `UIStackView` in iOS 9.
- [ExpyTableView](https://github.com/okhanokbay/ExpyTableView) - Make your table view expandable just by implementing one method. `Archived`
- [FileCards](https://github.com/etrep/FileCards_Swift) - A complete and modern OS X 10.10 Swift rewrite of Apple's FileCards example. `macOS`
- [files-ios](https://github.com/steventroughtonsmith/files-ios) - File Browser for iOS.
- [folding-cell](https://github.com/Ramotion/folding-cell) - :octocat: 📃 FoldingCell is an expanding content cell with animation made by @Ramotion `iOS`
- [GLTableCollectionView](https://github.com/giulio92/GLTableCollectionView) - Netflix and App Store like UITableView with UICollectionView, written in pure Swift 3.0. `iOS`
- [GodAnimation](https://github.com/daoinek/GodAnimation) - Simple animation for your views and cells.
- [HoverConversion](https://github.com/marty-suzuki/HoverConversion) - HoverConversion realized vertical paging with UITableView. UIViewController will be paged when reaching top or bottom of UITableView contentOffset. `Archived`
- [iOS-MultiSelectionTable](https://github.com/nunogoncalves/iOS-MultiSelectionTable) - Beautiful way of having a multi-selection table on iOS written in Swift. `iOS`
- [ios-swift-collapsible-table-section](https://github.com/jeantimex/ios-swift-collapsible-table-section) - A simple iOS swift project demonstrates how to implement collapsible table section.
- [JSONTableView](https://github.com/cemolcay/JSONTableView) - Expandable JSON data viewer. `iOS`
- [LUExpandableTableView](https://github.com/LaurentiuUngur/LUExpandableTableView) - A subclass of `UITableView` with expandable and collapsible section. `iOS`
- [MBTwitterScroll](https://github.com/martinblampied/MBTwitterScroll) - Recreate Twitter's profile page scrolling animation for UITableView and UIScrollViews.
- [MCMHeaderAnimated](https://github.com/mathcarignani/MCMHeaderAnimated) - MCMHeaderAnimated allows you to add an animation between list and detail views.
- [MYTableViewIndex](https://github.com/mindz-eye/MYTableViewIndex) - A pixel perfect replacement for UITableView section index, written in Swift.
- [NSTableView-Sections](https://github.com/krzyzanowskim/NSTableView-Sections) - NSTableView with sections (similar to UITableView) in Swift. `macOS`
- [NSTableView-Sorting](https://github.com/stevebartholomew/NSTableView-Sorting) - Drag Sorting NSTableView rows in Swift. `macOS`
- [PBDataTableView](https://github.com/praveenb-ios/PBDataTableView) - DataTable for iPhone and iPad.
- [PickerController](https://github.com/xiongxiong/PickerController) - Easy to use UITableViewCell implementing swiping to trigger actions (known from the Mailbox App).
- [QuickRearrangeTableView](https://github.com/okla/QuickRearrangeTableView) - Protocol-oriented solution to add quick cells rearrange/reorder to UITableView, written in Swift 2.2 `Archived`
- [RHPreviewCell](https://github.com/robertherdzik/RHPreviewCell) - Use long press on cell to trigger action I envied so much Spotify iOS app this great playlist preview cell, I decided to create my own ones. Now you can give your users ability to quick check "what content is hidden under your UITableViewCell". Great think is that this Library not requires 3D Touch support from user device.
- [SAStickyHeader](https://github.com/shams-ahmed/SAStickyHeader) - A very simple sticky header with multiple image support via swipe gestures.
- [SBGestureTableView](https://github.com/Stickbuilt/SBGestureTableView) - Swift UITableView subclass that supports swiping rows ala Mailbox and long press to move rows.
- [Static](https://github.com/venmo/Static) - Simple static table views for iOS in Swift.
- [StretchyHeaderView](https://github.com/sunlubo/StretchyHeaderView) - A generic stretchy header for UIScrollView, and allows you to change navigation bar's appearance dynamically.
- [SwipeAndSnapCell](https://github.com/iandundas/SwipeAndSnapCell) - Cell which immitates iOS10's Mail.app cell swiping behavior.
- [SwipeCellKit](https://github.com/SwipeCellKit/SwipeCellKit) - Swipeable UITableViewCell based on the stock Mail.app, implemented in Swift. `iOS` `UIKit`
- [SwipyCell](https://github.com/moritzsternemann/SwipyCell) - Easy to use UITableViewCell implementing swiping to trigger actions (known from the Mailbox App). `iOS`
- [TableFlip](https://github.com/mergesort/TableFlip) - A simpler way to do cool UITableView animations. `iOS`
- [TableView-PullToRefresh](https://github.com/vinit5320/TableView---PullToRefresh) - Guide: https://swiftyos.wordpress.com/2015/09/29/animated-tableview-pull-to-refresh-loading-pulltobounce
- [TableViewDragger](https://github.com/KyoheiG3/TableViewDragger) - A cells of UITableView can be rearranged by drag and drop. `iOS`
- [Tabman](https://github.com/uias/Tabman) - A powerful paging view controller with indicator bar for iOS. `iOS`
- [TanibleView](https://github.com/dokgi88/TanibleView) - Veeeeeeeeeeeeeeeery easy to use and simple animate TableView `iOS`
- [UITableViewCellAnimation](https://github.com/V8tr/UITableViewCellAnimation-Article-Final) - The project demonstrates how to animate UITableViewCells when they first appear on a screen. `iOS`
- [UITableViewPushAnimation](https://github.com/pal2tapas/UITableViewPushAnimation) - Push a UIViewController with a attractable animation from UITableView.
- [VPAccordionAnimation](https://github.com/varunpm1/VPAccordionAnimation) - Accordion Animation for UITableView cell expansion and collapsing.
- [WCSTimeline](https://github.com/WrightsCS/WCSTimeline) - Simple timeline with data model.
- [WLEmptyState](https://github.com/WizelineLabs/WLEmptyState) - WLEmptyState is an iOS based component that lets you customize the view when the dataset of UITableView is empty. `iOS` `UIKit`
- [WobbleView](https://github.com/dotintent/WobbleView) -  Wobble effect.
- [YNExpandableCell](https://github.com/younatics/YNExpandableCell) - ✨ Awesome expandable, collapsible tableview cell for iOS written in Swift 4 `iOS`
- [ZYThumbnailTableView](https://github.com/liuzhiyi1992/ZYThumbnailTableView) - a TableView have thumbnail cell only, and you can use gesture let it expands other expansionView, all diy.

## Navigation and presentation

### Action sheets

- [FloatingActionSheetController](https://github.com/ra1028/FloatingActionSheetController) - Cool design ActionSheetController library written in Swift2.
- [KUIActionSheet](https://github.com/Kofktu/KUIActionSheet) - Custom UIActionSheet.
- [PCRapidSelectionView](https://github.com/mmackh/PCRapidSelectionView) - Interactive, beautiful & fast UIActionSheet replacement, supports continuous hold & select.
- [PPAssetsActionController](https://github.com/pavelpantus/PPAssetsActionController) - Highly customizable Action Sheet Controller with Assets Preview written in Swift 3.
- [Sheeeeeeeeet](https://github.com/danielsaidi/Sheeeeeeeeet) - Sheeeeeeeeet is a Swift library for custom action sheets. `iOS`
- [SheetViewController](https://github.com/bananaRanger/SheetViewController) - SheetViewController - is a customizable native-like sheet alert controller. `iOS`
- [XLActionController](https://github.com/xmartlabs/XLActionController) - Fully customizable and extensible action sheet controller written in Swift 2. `iOS`

### Alerts and notifications

- [AANotifier](https://github.com/EngrAhsanAli/AANotifier) - AANotifier allows you to create UIView based fragments to be appear on screen at runtime in iOS, written in Swift.
- [Alertift](https://github.com/sgr-ksmt/Alertift) - Swifty, modern UIAlertController wrapper. `UIKit` `Archived`
- [AlertKit](https://github.com/sparrowcode/AlertKit) - Native alert from Apple Music & Feedback. Contains Done, Heart & Message and other presets. `iOS` `SwiftUI` `UIKit`
- [alerts-and-pickers](https://github.com/dillidon/alerts-and-pickers) - Advanced usage of UIAlertController and pickers based on it: Telegram, Contacts, Location, PhotoLibrary, Country, Phone Code, Currency, Date...
- [AlertToast](https://github.com/elai950/AlertToast) - Alert Toast is an open-source library in Github to use with SwiftUI. It allows you to present popups that don't need any user action to dismiss or to validate. `SwiftUI`
- [AlertViewController](https://github.com/stringcode86/AlertViewController) - UIAlertController subclass to show image above the alert title.
- [AMTooltip](https://github.com/amirdew/AMTooltip) - Simple and easy library to show tooltip in iOS. `Archived`
- [AppRatingAlert-Swift](https://github.com/pablojotaguardiola/AppRatingAlert-Swift) - iOS AlertView to the user can rate your App.
- [ASToast](https://github.com/abdullahselek/ASToast) - A Swift extension for using Android style Toast notifications.
- [AwaitToast](https://github.com/k-lpmg/AwaitToast) - Basic toast as well as async waiting toast. Inspired by facebook posting toast. `iOS`
- [AZDialogViewController](https://github.com/Minitour/AZDialogViewController) - A highly customizable alert dialog controller that mimics Snapchat's alert dialog.
- [AZNotification-Swift](https://github.com/azamsharp/AZNotification-Swift)
- [Bauletto](https://github.com/gianpispi/Bauletto) - Display iOS 13 style banner with ease. `iOS`
- [BisKit](https://github.com/ho0t/BisKit) - BisKit is an iOS library to generate beautiful popups as the one featured when Apple Pencil is attached to the new iPad Pro.
- [BMInputBox](https://github.com/blackmirror-media/BMInputBox) - BMInputBox `Archived`
- [BRYXBanner](https://github.com/bryx-inc/BRYXBanner) - A lightweight dropdown notification for iOS 7+, in Swift.
- [BulletinBoard](https://github.com/alexaubry/BulletinBoard) - Generate and Display Bottom Card Interfaces on iOS. `iOS`
- [CDAlertView](https://github.com/candostdagdeviren/CDAlertView) - Highly customizable alert/notification/success/error/alarm popup written in Swift 3.
- [CFAlertViewController](https://github.com/Codigami/CFAlertViewController) - It is a highly configurable iOS library which allows easy styling with built in styles as well as extra header and footer views so that you can make extremely unique alerts and action sheets.
- [CleanyModal](https://github.com/loryhuz/CleanyModal) - Swift Kit to present clean modal/alert.
- [CPAlertViewController](https://github.com/katafo/CPAlertViewController) - A way to create a custom alert view with animation.
- [CRNotifications](https://github.com/dkcas11/CRNotifications) - Custom in-app notifications.
- [CustomAlertView](https://github.com/DrankoLQ/CustomAlertView) - Enhanced AlertView that extends UIViewController. `iOS`
- [CWStatusBarNotification](https://github.com/cezarywojcik/CWStatusBarNotification) - A library that allows you to easily create text-based notifications that appear on the status bar.
- [DCAlertController](https://github.com/noppefoxwolf/DCAlertController) - Alert like Android wear(Delay Confirm)
- [DOAlertController](https://github.com/okmr-d/DOAlertController) - Simple Alert View written in Swift, which can be used as a UIAlertController. (AlertController/AlertView/ActionSheet)
- [Dodo](https://github.com/evgenyneu/Dodo) - A message bar for iOS written in Swift. `iOS`
- [DPNotify](https://github.com/dphans/DPNotify) - DPNotify used to send short notifications on screen simple & quickly for iOS developing using Swift.
- [Drops](https://github.com/omaralbeik/Drops) - A µFramework for showing alerts like the one used when copying from pasteboard or connecting Apple pencil. `iOS` `SwiftUI` `UIKit`
- [DTIToastCenter-Swift](https://github.com/dtissera/DTIToastCenter-Swift) - A toast center for displaying quick toast to the user.
- [DTLocalNotification](https://github.com/tungvoduc/DTLocalNotification) - Custom control that makes displaying in-app notifications easier, cleaner and more efficient. `iOS`
- [EasyTipView](https://github.com/teodorpatras/EasyTipView) - Fully customisable tooltip view in Swift for iOS. `Archived`
- [EFInternetIndicator](https://github.com/ezefranca/EFInternetIndicator) - ❌📱 A little swift Internet error status indicator using ReachabilitySwift
- [EZAlertController](https://github.com/thellimist/EZAlertController) - Easy Swift UIAlertController.
- [FTPopOverMenu_Swift](https://github.com/liufengting/FTPopOverMenu_Swift) - FTPopOverMenu_Swift, swift version of FTPopOverMenu.
- [GLNotificationBar](https://github.com/gokulgovind/GLNotificationBar) - GLNotificationBar is a ios10 style notification bar, can be used to handle push notification in active state. `iOS`
- [Hermes](https://github.com/Imgur/Hermes) `Archived`
- [HJToast](https://github.com/himanshujoshi47/HJToast) - Toast messages for iOS.
- [HYAlertController](https://github.com/iafine/HYAlertController) - A Simple And Minimalist iOS AlertController.
- [Indicate](https://github.com/pkluz/Indicate) - Interactive notification pop-over (aka "Toast) modeled after the iOS AirPods and Apple Pencil indicator.
- [iOSNotificationBanner](https://github.com/elarahq/iOSNotificationBanner) `Archived`
- [iPopUp](https://github.com/BlueWonders/iPopUp) - iPopUp uses custom view, not UIPopover or AlertView. UIView contains a tableview. The project is simple, clean and easy to implement.
- [JHTAlertController](https://github.com/jjessel/JHTAlertController) - A custom iOS alert that replaces the stock UIAlertController. Easily style the alert to match your app. Written in Swift for iOS. `iOS`
- [KCustomAlert](https://github.com/krishnads/KCustomAlert) - Simple and easy alerts to use instead of default AlertController. Separate Xib is provided to customize as pr your need. Callbacks are easily handled by using Closures. `iOS`
- [KRAlertController](https://github.com/krimpedance/KRAlertController) - A colored alert view for your iOS. `Archived`
- [KUIPopOver](https://github.com/Kofktu/KUIPopOver) - Easy to use PopOver in iOS. `iOS`
- [Loaf](https://github.com/schmidyy/Loaf) - A Swifty Framework for Easy iOS Toasts.
- [LPSnackbar](https://github.com/luispadron/LPSnackbar) - A flexible and easy to use Snackbar control for iOS. `iOS` `UIKit` `Archived`
- [Malert](https://github.com/vitormesquita/Malert) - Custom alert View to iOS applications. `iOS`
- [MIAlertController](https://github.com/MarioIannotta/MIAlertController) - A simple fully customizable alert controller. `Archived`
- [NavigationNotice](https://github.com/KyoheiG3/NavigationNotice) - Customizable and interactive animated notification UI control.
- [NeatTipView](https://github.com/rootstrap/NeatTipView) - NeatTipView allows you to display message tooltips that can be used as call to actions or informative tips. `iOS`
- [Notie](https://github.com/thii/Notie) - In-app notification in Swift, with customizable buttons and input text field.
- [Notification-AlertView](https://github.com/appus-studio/Notification-AlertView)
- [NotificationBanner](https://github.com/Daltron/NotificationBanner) - The easiest way to display highly customizable in app notification banners in iOS. `iOS`
- [NotificationToast](https://github.com/PhilippeWeidmann/NotificationToast) - A view that tries to replicate iOS default toast message view. `iOS` `SwiftUI` `UIKit`
- [NotificationView](https://github.com/pikachu987/NotificationView) - iOS Basic Notification screens.
- [PathDynamicModal](https://github.com/ra1028/PathDynamicModal) - A modal view using UIDynamicAnimator, like the Path for iOS.
- [PMAlertController](https://github.com/pmusolino/PMAlertController) - PMAlertController is a great and customizable substitute to UIAlertController.
- [PokeModal](https://github.com/lborgav/PokeModal) - Simple Modal View inspired Pokémon GO written in Swift.
- [PokerCard](https://github.com/iWeslie/PokerCard) - A new generation of Alert View with fluid design.
- [Popover](https://github.com/corin8823/Popover) - Popover is a balloon library like Facebook app. It is written in pure swift.
- [Popover-label](https://github.com/eonist/Popover-label) - Popover label for iOS. `iOS`
- [PopupDialog](https://github.com/Orderella/PopupDialog) - A simple, customizable popup dialog for iOS written in Swift. Replaces UIAlertControllers alert style.
- [PopupView](https://github.com/exyte/PopupView) - Toasts and popups library written with SwiftUI. `SwiftUI`
- [RNNotificationView](https://github.com/souzainf3/RNNotificationView) - Emulates the native Notification Banner UI for any alert.
- [SCLAlertView-Swift](https://github.com/vikmeup/SCLAlertView-Swift) - Beautiful animated Alert View. Written in Swift
- [ScrollableDisclaimerAlert](https://github.com/kubacizek/ScrollableDisclaimerAlert) - Simple lightweight DisclaimerAlertView. `Archived`
- [SHSnackBarView](https://github.com/iamshezad/SHSnackBarView) - SHSnackBarView is a simple library for snackbar type alert in swift.
- [Siren](https://github.com/ArtSabintsev/Siren) - Notify users when a new version of your iOS app is available, and prompt them with the App Store link.
- [Snackbar-iOS](https://github.com/sneiko/Snackbar-iOS) - Simple snackbar for ios from android platform. `iOS`
- [SpaceView](https://github.com/Xopoko/SpaceView) `iOS`
- [SPIndicator](https://github.com/ivanvorobei/SPIndicator) - Floating indicator, mimicrate to indicator which appear when silent mode turn on / off. Support large texts. `UIKit`
- [Squawk](https://github.com/GitHawkApp/Squawk) - Quick & interactive iOS alerts in Swift. `UIKit`
- [StatusAlert](https://github.com/LowKostKustomz/StatusAlert) - Display Apple system-like self-hiding status alerts. It is well suited for notifying user without interrupting user flow in iOS-like way. `iOS` `UIKit`
- [SweetAlert-iOS](https://github.com/codestergit/SweetAlert-iOS) - Live animated Alert View for iOS written in Swift
- [Swift-Prompts](https://github.com/GabrielAlva/Swift-Prompts) - A Swift library to design custom prompts with a great scope of options to choose from.
- [SwiftEntryKit](https://github.com/huri000/SwiftEntryKit) - SwiftEntryKit is a banner presenter library for iOS. It can be used to easily display pop-ups and notification-like views within your iOS apps.
- [SwiftMessages](https://github.com/SwiftKickMobile/SwiftMessages) - A very flexible message bar for iOS written in Swift. `iOS` `SwiftUI` `UIKit`
- [SwiftNotify](https://github.com/JT501/SwiftNotify) - A Swifty UI framework for notifications and alerts. `iOS` `UIKit`
- [SwiftyDrop](https://github.com/morizotter/SwiftyDrop) - Lightweight dropdown message bar in Swift. It's simple and beautiful. `Archived`
- [SwiftyPickerPopover](https://github.com/hsylife/SwiftyPickerPopover) - Popover with Picker by Swift 3/2.3 for iPhone/iPad, iOS9+.
- [TKSwarmAlert](https://github.com/takuoka/TKSwarmAlert) - Animated alert library like Swarm app.
- [Toast](https://github.com/Hengyu/Toast) - A Swift Toast view - iOS 14 style - built with UIKit. `iOS` `UIKit`
- [Toast-Swift](https://github.com/scalessec/Toast-Swift) - A Swift extension that adds toast notifications to the UIView object class.
- [Toast-Swift](https://github.com/BastiaanJansen/toast-swift) - A Swift Toast view - iOS 14 style - built with UIKit. `iOS` `UIKit`
- [ToastUI](https://github.com/quanshousio/ToastUI) - A simple way to show toast in SwiftUI. `SwiftUI`
- [TrophyKit](https://github.com/xnth97/TrophyKit) - An animated trophy banner that looks like Xbox achievement. `iOS` `tvOS` `UIKit`
- [TTGSnackbar](https://github.com/zekunyan/TTGSnackbar) - TTGSnackbar shows simple message and action button on the bottom or top of the screen with multi kinds of animation. `iOS`
- [UNAlertView](https://github.com/ytakzk/UNAlertView) - Flexible and simple UIAlertView replacement.
- [VKPopupView](https://github.com/vladislav-k/VKPopupView) - Lightweight and easy to use blurred popup view written in Swift. You will find it very similar to your iOS folders at Springboard (Home screen).
- [Whisper](https://github.com/hyperoslo/Whisper) - Whisper is a component that will make the task of display messages and in-app notifications simple. It has three different views inside. `iOS`
- [Xia](https://github.com/iTofu/Xia) - Naughty flexible alert view above the navigation bar.
- [ZKNavigationController](https://github.com/ZacharyKhan/ZKNavigationController) - iOS Navigation Controller Alert. `Archived`

### Cards

- [Cards](https://github.com/PaoloCuscela/Cards) - Awesome iOS 11 appstore cards in swift 4. `iOS` `UIKit`
- [cardslider](https://github.com/Ramotion/cardslider) -  Cardslider is a design UI controller that allows you to swipe through cards with pictures and accompanying descriptions. `iOS`
- [CardSlider](https://github.com/saoudrizwan/CardSlider) - Innovative twist to Tinder cards for iOS. `iOS`
- [CardsStack](https://github.com/priteshrnandgaonkar/CardsStack) - An awesome set of cards at your disposal `iOS`
- [HFCardCollectionViewLayout](https://github.com/hfrahmann/HFCardCollectionViewLayout) - The HFCardCollectionViewLayout provides a card stack layout not quite similar like the apps Reminder and Wallet. `iOS` `Archived`
- [iCard](https://github.com/eliakorkmaz/iCard) - Bank Card Generator with Swift using SnapKit DSL. `iOS`
- [Koloda](https://github.com/Yalantis/Koloda) - KolodaView is a class designed to simplify the implementation of Tinder like cards on iOS. `iOS`
- [MaterialCardView](https://github.com/cemolcay/MaterialCardView) - Create material design cards quick and easy
- [MGSwipeCards](https://github.com/mac-gallagher/MGSwipeCards) - A flexible, multi-directional card swiping framework inspired by Tinder. `iOS` `Archived`
- [MMCardView](https://github.com/MillmanY/MMCardView) - Custom CollectionView like Wallet App.
- [SCCardView](https://github.com/myoungsc/SCCardView) - Select Card Change View Content.
- [ScrollingCardView](https://github.com/mozilla-mobile/ScrollingCardView) - A card view widget for iOS that will grow with its content, enabling scrolling when the content is larger than the view. `Archived`
- [SwiftUI-CardStackView](https://github.com/dadalar/SwiftUI-CardStackView) - A easy-to-use SwiftUI view for Tinder like cards on iOS, macOS & watchOS. `SwiftUI`
- [VerticalCardSwiper](https://github.com/JoniVR/VerticalCardSwiper) - A marriage between the Shazam Discover UI and Tinder, built with UICollectionView in Swift. `iOS` `UIKit`

### Menus

- [AirBar](https://github.com/uptechteam/AirBar) - UIScrollView driven expandable menu. `iOS`
- [BTNavigationDropdownMenu](https://github.com/PhamBaTho/BTNavigationDropdownMenu) - The elegant dropdown menu, written in Swift, appears underneath navigation bar to display a list of related items when a user click on the navigation title. `iOS`
- [circle-menu](https://github.com/Ramotion/circle-menu) - CircleMenu is a simple, elegant menu with a circular layout. `iOS`
- [ContextMenu](https://github.com/GitHawkApp/ContextMenu) - An iOS context menu UI inspired by Things 3. `iOS` `UIKit`
- [DPEdgeMenu-Swift](https://github.com/HongliYu/DPEdgeMenu-Swift) - Simple menu appear from four directions of screen edge. `Archived`
- [DropDown](https://github.com/AssistoLab/DropDown) - A Material Design drop down for iOS.
- [DropDownMenuKit](https://github.com/qmathe/DropDownMenuKit) - UIKit drop down menu, simple yet flexible and written in Swift. `iOS` `UIKit`
- [DSFQuickActionBar](https://github.com/dagronf/DSFQuickActionBar) - A spotlight-inspired quick action bar for macOS. `macOS` `SwiftUI` `AppKit`
- [EasyDropdown](https://github.com/onmyway133/EasyDropdown) - :droplet: Fantastic dropdown in Swift `iOS`
- [ENSwiftSideMenu](https://github.com/devgenios/ENSwiftSideMenu) - A lightweight flyover side menu component for iOS with the UIDynamic's bouncing animation, UIGestures and UIBlurEffect.
- [ExpandingMenu](https://github.com/monoqlo/ExpandingMenu) - ExpandingMenu is menu button for iOS written in Swift.
- [FAPanels](https://github.com/fahidattique55/FAPanels) - FAPanels - Swift.
- [FatSidebar](https://github.com/CleanCocoa/FatSidebar) - Custom vertical button toolbar for macOS. `macOS`
- [FlowingMenu](https://github.com/yannickl/FlowingMenu) - Interactive view transition to display menus with flowing and bouncing effects in Swift.
- [gmenu](https://github.com/amirdew/gmenu) - A redesigned menu for Gmail iOS app, implemented using SwiftUI. `iOS` `SwiftUI` `Archived`
- [GNAContextMenu](https://github.com/gridNA/GNAContextMenu) - Long press context menu (like in Pintrest for iOS app).
- [GuillotineMenu](https://github.com/Yalantis/GuillotineMenu) - Our Guillotine Menu Transitioning Animation implemented in Swift reminds a bit of a notorious killing machine. `iOS`
- [Hamburger-DropMenu](https://github.com/vinit5320/Hamburger-DropMenu) - Guide: https://swiftyos.wordpress.com/2016/03/10/animated-hamburger-dropdown-menu-nkdropdownmenu/
- [HHDropDownList](https://github.com/Herbert77/HHDropDownList) - 具备下滑动效的选项列表按钮.
- [Hokusai](https://github.com/ytakzk/Hokusai) - Swift library that provides a bouncy action sheet. `iOS` `UIKit`
- [JGFlipMenu](https://github.com/ziligy/JGFlipMenu) - Flipping menu system written in Swift. Uses @IBDesignable for quick and easy implementation.
- [KYWheelTabController](https://github.com/ykyouhei/KYWheelTabController) - KYWheelTabController is a subclass of UITabBarController.It displays the circular menu instead of UITabBar.
- [MarkingMenu](https://github.com/FlexMonkey/MarkingMenu) - Swift MarkingMenu
- [MaterialTapTargetPrompt](https://github.com/Abedalkareem/MaterialTapTargetPrompt-iOS) - A iOS version of Material Tap Target Prompt. `iOS`
- [MediumMenu](https://github.com/pixyzehn/MediumMenu) - A menu based on Medium iOS app. `Archived`
- [Menu](https://github.com/simsaens/Menu) - The iOS Menu.
- [Menu](https://github.com/iSapozhnik/Menu) - The most customizable menu for macOS apps. `macOS`
- [MenuController](https://github.com/anmolrajpal/MenuController) - An easy-to-use Action Menu Modal Controller inspired by iOS 13 Apple's native app implementation.
- [MenuItemKit](https://github.com/cxa/MenuItemKit) - MenuItemKit provides image and block(closure) support for UIMenuItem. `Archived`
- [MTSideMenubar](https://github.com/manekdilip/MTSideMenubar) - Side menu bar creating easily left and right side.
- [PageMenu](https://github.com/PageMenu/PageMenu) - A paging menu controller built from other view controllers placed inside a scroll view (like Spotify, Windows Phone, Instagram).
- [Side-Menu.iOS](https://github.com/Yalantis/Side-Menu.iOS) - Animated side menu with customizable UI. `iOS`
- [SideMenuController](https://github.com/teodorpatras/SideMenuController) - A side menu controller written in Swift. `Archived`
- [SidePanel](https://github.com/db42/SidePanel) - Google styled side panel for iOS written in Swift.
- [SlideMenuControllerSwift](https://github.com/dekatotoro/SlideMenuControllerSwift) - iOS Slide Menu View based on Google+, iQON, Feedly, Ameba iOS app. It is written in pure swift.
- [SliderPanel](https://github.com/sebk/SliderPanel) - Slidable Panel in Swift
- [SphereMenuSwift](https://github.com/caamorales/SphereMenuSwift) - A port of itouch2's https://github.com/itouch2/SphereMenu to Swift
- [Summflower](https://github.com/iSame7/Summflower) - Swift implementation to the sexiest sharing icon based on Summly app.
- [SvpplyTable](https://github.com/666lm/SvpplyTable) - Expandable and collapsable Menu, like Svpply.
- [SwiflyOverlay](https://github.com/edwinbosire/SwiflyOverlay) - Another Navigation component for iOS. This time written in swift.
- [Swift-CircleMenu](https://github.com/hu55a1n1/Swift-CircleMenu) - Rotating circle menu written in Swift 3. `Archived`
- [SwiftShareBubbles](https://github.com/takecian/SwiftShareBubbles) - Animated Social share buttons control for iOS written in Swift.
- [SwiftyMenu](https://github.com/KarimEbrahemAbdelaziz/SwiftyMenu) - Drop down menu for iOS. `iOS`
- [SwiftySideMenu](https://github.com/hossamghareeb/SwiftySideMenu) - SwiftySideMenu is a lightweight and easy to use side menu controller to add left menu and center view controllers with scale animation based on Pop framework.
- [VTSwiftySlideMenu](https://github.com/vinhnotes/VTSwiftySlideMenu) - An iOS navigation menu with Split-View supported on iPad and iPhone XS Max.
- [YNDropDownMenu](https://github.com/younatics/YNDropDownMenu) - Awesome iOS drop down menu with Swift 3. `iOS`

### Navigation bars

- [ADNavigationBarExtension](https://github.com/faberNovel/ADNavigationBarExtension) - iOS UI library to show and hide an extension to your UINavigationBar. `Archived`
- [AMScrollingNavbar](https://github.com/andreamazz/AMScrollingNavbar) - Scrollable UINavigationBar that follows the scrolling of a UIScrollView.
- [Bartinter](https://github.com/MaximKotliar/Bartinter) - Changes your status bar depending on content behind it. `UIKit`
- [BusyNavigationBar](https://github.com/gmertk/BusyNavigationBar) - A UINavigationBar extension to show loading effects above navigation bar's background.
- [CardNavigation](https://github.com/james01/CardNavigation) - A navigation controller that displays its view controllers as an interactive stack of cards. `iOS` `UIKit`
- [DropdownTitleView](https://github.com/GitHawkApp/DropdownTitleView) - A UINavigationItem.titleView compatible UIControl with a title, subtitle, and dropdown.
- [ImageInNavigationBarDemo](https://github.com/tungfam/ImageInNavigationBarDemo) - Demo project that shows a resizable image in right top corner of Navigation Bar with Large Title (iOS11).
- [KJNavigationViewAnimation](https://github.com/KiranJasvanee/KJNavigationViewAnimation) - Custom navigation view animation based on dragging & scrolling at TableView, CollectionView OR ScrollView
- [MTCoordinatorView](https://github.com/mittsu333/MTCoordinatorView) - The view coordinate arranged to the scrolling is adjusted. `Archived`
- [navigation-stack](https://github.com/Ramotion/navigation-stack) - NavigationStack is a stack-modeled navigation controller. `iOS`
- [PagingKit](https://github.com/kazuhiro4949/PagingKit) - PagingKit provides customizable menu UI. It has more flexible layout and design than the other libraries. `iOS` `UIKit`
- [SAHistoryNavigationViewController](https://github.com/marty-suzuki/SAHistoryNavigationViewController) - iOS task manager like UI in UINavigationContoller. Support 3D Touch. `Archived`
- [SPFakeBar](https://github.com/ivanvorobei/SPFakeBar) - Very similar to original Navigation Bar. Full customisable.
- [Tamamushi](https://github.com/makomori/Tamamushi) - Gradient NavigationBar library written in Swift.
- [TB_TwitterUI](https://github.com/ariok/TB_TwitterUI) - This is the code for the ThinkAndBuild tutorial: "Implementing the Twitter App UI" (WIP)
- [TinderNavDemo](https://github.com/imaccallum/TinderNavDemo) - Tinder-style parallax paging navigation implementation.
- [TwitterAnimation](https://github.com/saifhunk/TwitterAnimation) - Twitter animation with strechty header and tableview cells with differnt type
- [WhiteNavigationController](https://github.com/Zandor300/WhiteNavigationController) - A White UINavigationBar like in Apple's apps. `iOS` `UIKit`

### Onboarding

- [Ajimi](https://github.com/nakajijapan/Ajimi) - Ajimi means tasting. In Japanese, 味見. Ajimi is the feedback tool, which anyone can easily feedback to project team any time. `iOS`
- [BWWalkthrough](https://github.com/ariok/BWWalkthrough) - BWWalkthrough is a class to build custom walkthroughs for your iOS App.
- [ConcentricOnboarding](https://github.com/exyte/ConcentricOnboarding) - SwiftUI library for a walkthrough or onboarding flow with tap actions. `iOS` `SwiftUI`
- [Gecco](https://github.com/xai3/Gecco) - Simply highlight items for your tutorial walkthrough, written in Swift.
- [GLWalkthrough](https://github.com/gokulgovind/GLWalkthrough) - GLWalkthrough is an easily configurable plug-and-play tool to add walkthrough or coachmarker functionality to your app with ease. `iOS`
- [HAPlayerView](https://github.com/litoarias/HAPlayerView) - Easy-to-use class for inserting videos as a wallpaper without a single line of code, all managed by Interface Builder.
- [ImageBlur](https://github.com/yogesh07-ios/ImageBlur) - Blur out the image portion were user drag his/her finger.
- [Instructions](https://github.com/ephread/Instructions) - Create walkthroughs and guided tours (coach marks) in a simple way, with Swift.
- [JTSplashView](https://github.com/kubatruhlar/JTSplashView) - Create the beautiful splash view with JTSplashView.
- [KJOverlayTutorial](https://github.com/tranquan/KJOverlayTutorial) - A Tutorial for iOS.
- [LaunchScreenSnapshot](https://github.com/alexruperez/LaunchScreenSnapshot) - Protects sensitive data in your app snapshot. `iOS`
- [material-showcase-ios](https://github.com/aromajoin/material-showcase-ios) - An elegant way to guide your beloved users in iOS apps - Material Showcase.
- [Minamo](https://github.com/xai3/Minamo) - Simple coach mark library written in Swift.
- [OnboardingKit](https://github.com/Athlee/OnboardingKit) - A simple and interactive framework for making iOS onboarding experience easy and fun.
- [paper-onboarding](https://github.com/Ramotion/paper-onboarding) - PaperOnboarding is a material design slider. `iOS`
- [Presentation](https://github.com/hyperoslo/Presentation) - Presentation helps you to make tutorials, release notes and animated pages. `iOS`
- [PRGTipView](https://github.com/ispiropoulos/PRGTipView) - PRGTipView is a drop-in solution for adding onboarding tips to your apps.
- [RevealingSplashView](https://github.com/PiXeL16/RevealingSplashView) - A Splash view that animates and reveals its content, inspired by Twitter splash.
- [RMParallax](https://github.com/michaelbabiy/RMParallax) - The way to impress users on the first app launch.
- [SoundCloudTransition](https://github.com/xxxAIRINxxx/SoundCloudTransition) - Custom interactive transition like SoundCloud iOS App.
- [SplashWindow](https://github.com/RnBlue8/SplashWindow) - An UIWindow-based TouchID authentication control.
- [Spotlight](https://github.com/lekshmiraveendranath/Spotlight) - Introductory walkthrough framework for iOS Apps.
- [SuggestionsKit](https://github.com/AlphanumericCharactersOrSingleHyphenz/SuggestionsKit) - SuggestionsKit is a framework for iOS that was created in order to provide developers with the opportunity to educate users on various features of applications.
- [SwiftUI-OnBoarding-Screen-Animation](https://github.com/guendev/SwiftUI-OnBoarding-Screen-Animation)
- [SwiftyOnboard](https://github.com/juanpablofernandez/SwiftyOnboard) - A swifty iOS framework that allows developers to create beautiful onboarding experiences. `iOS` `Archived`
- [SwiftyWalkthrough](https://github.com/ruipfcosta/SwiftyWalkthrough) - The easiest way to create a great walkthrough experience in your apps, powered by Swift.
- [tween-controller](https://github.com/daltonclaybrook/tween-controller) - A toolkit for creating interactive menus and tutorials in Swift.
- [TwitterBirdAnimation](https://github.com/rounak/TwitterBirdAnimation) - Twitter bird animation
- [TZConfettiIntro](https://github.com/tahseen0amin/TZConfettiIntro) - Intro Pages with Confetti. Instead of having a dull Intro pages, you can use confetti to make it more presentable.
- [VideoSplashKit](https://github.com/sahin/VideoSplashKit) - VideoSplashKit - UIViewController library for creating easy intro pages with background videos

### Page indicators

- [CHIPageControl](https://github.com/ChiliLabs/CHIPageControl) - A set of cool animated page controls written in Swift to replace boring UIPageControl. `iOS`
- [FlexiblePageControl](https://github.com/shima11/FlexiblePageControl) - A flexible PageControl like Instagram. `iOS`
- [GBPageControl](https://github.com/jhurt/GBPageControl) - A page control for SpriteKit based games written in Swift.
- [ISPageControl](https://github.com/Interactive-Studio/ISPageControl) - A page control similar to that used in Instagram. `iOS`
- [MBPageControl](https://github.com/c-Viorel/MBPageControl) - A highly customizable page control for OS X. `macOS`
- [PageControls](https://github.com/popwarsweet/PageControls) - This is a selection of custom page controls to replace UIPageControl, inspired by a dribbble.
- [TKRubberIndicator](https://github.com/tbxark/TKRubberIndicator) - A rubber animation pagecontrol. `iOS` `UIKit`

### Pagers

- [HQPagerViewController](https://github.com/quangpc-zz/HQPagerViewController) - This control combines the great menu view with a UIPageviewController that takes care of showing the right page when clicking on the menu view and updating the selection when the UIPageviewController scrolls.
- [PageController](https://github.com/hirohisa/PageController) - PageController is infinite paging controller, scrolling through contents and title bar scrolls with a delay. Then it provide user interaction to smoothly and effortlessly moving. It is for iOS written in Swift.
- [PagerTabStripView](https://github.com/xmartlabs/PagerTabStripView) - An easy to use view pager library for iOS in Swift. `SwiftUI`
- [PBPagerViewController](https://github.com/paoloboschini/PBPagerViewController) - A Swifty Pager View Controller
- [ViewPager](https://github.com/SeptiyanAndika/ViewPager---Swift) - Simple View Pager library for Swift. `Archived`

### Panels and bottom sheets

- [ActionPicker](https://github.com/Krivoblotsky/ActionPicker) - My humble effort to mimic iOS setup sheets.
- [Aiolos](https://github.com/IdeasOnCanvas/Aiolos) - A floating panel for your iOS Apps. `iOS` `UIKit`
- [Arrows](https://github.com/antoniocasero/Arrows) - Arrows is an animated custom view to give feedback about your UI sliding panels.
- [AYPullBoard](https://github.com/bananaRanger/AYPullBoard) - Сustomized pull board based on your view. `iOS`
- [BottomSheet](https://github.com/finn-no/BottomSheet) - BottomSheet is an implementation of custom modal presentation style for thumb-friendly interactive views anchored to the bottom of the screen. `iOS`
- [BottomSheet](https://github.com/lucaszischka/BottomSheet) - A sliding Sheet from the bottom of the Screen with 3 States build with SwiftUI. `SwiftUI`
- [BottomSheetController](https://github.com/naru-jpn/BottomSheetController) - UIKit component containing supplementary content that are anchored to the bottom of the screen. `UIKit`
- [BottomSheetDemo](https://github.com/MFiOSDemos/BottomSheetDemo)
- [ContainerController](https://github.com/mrustaa/ContainerController) - 👉↕️📱ContainerController 🧩✨⚙️ is a UI Component Swipe-Panel (Customizable). 💡 The idea is copied from the app: Apple Maps, Stocks. Swift version `iOS`
- [DeckTransition](https://github.com/HarshilShah/DeckTransition) - A library to recreate the iOS 10 Apple Music now playing transition. `iOS`
- [drawer-view](https://github.com/eleev/drawer-view) - Drawer View is a custom UI component replication of Apple's Apple Music player and Shortcuts components view. `iOS` `UIKit`
- [DrawerKit](https://github.com/babylonhealth/DrawerKit) - DrawerKit lets an UIViewController modally present another UIViewController in a manner similar to the way Apple's Maps app works. `iOS` `UIKit`
- [DTContainerController](https://github.com/tungvoduc/DTContainerController) - A Swift container view controller to handle transitioning to a different child view controller.
- [DTOverlayController](https://github.com/tungvoduc/DTOverlayController) - A customizable and easy-to-use overlay view controller container. `UIKit`
- [FloatingPanel](https://github.com/scenee/FloatingPanel) - A clean and easy-to-use floating panel UI component for iOS.
- [GTSheet](https://github.com/gametimesf/GTSheet) - An easy to integrate solution for presenting UIViewControllers in a bottom sheet. `iOS` `Archived`
- [InteractiveCardViewAnimation](https://github.com/brianadvent/InteractiveCardViewAnimation)
- [MCPanelViewController](https://github.com/matthewcheok/MCPanelViewController) - Drop-in panel control.
- [MIBlurPopup](https://github.com/MarioIannotta/MIBlurPopup) - MIBlurPopup let you create amazing popups with a blurred background.
- [OverlayContainer](https://github.com/gaetanzanella/OverlayContainer) - Non-intrusive iOS UI library to implement overlay based interfaces - [Blog post](https://gaetanzanella.github.io/2018-12-17/replicating-apple-maps-overlay) `iOS` `UIKit`
- [Panelkit](https://github.com/louisdh/panelkit) - A UI framework that enables panels on iOS. `iOS` `UIKit` `Archived`
- [Panels](https://github.com/antoniocasero/Panels) - Panels is a framework to easily add sliding panels to your application.
- [PanModal](https://github.com/slackhq/PanModal) - An elegant and highly customizable presentation API for constructing bottom sheet modals on iOS. `Archived`
- [PartialSheet](https://github.com/AndreaMiotto/PartialSheet) - A custom SwiftUI modifier to present a Partial Modal Sheet. `SwiftUI`
- [PresentationControllerBlog](https://github.com/kylebshr/PresentationControllerBlog) - Custom UIPresentationController project for https://kylebashour.com/posts/custom-view-controller-presentation-tips
- [Pulley](https://github.com/52inc/Pulley) - A library to imitate the iOS 10 Maps UI. `iOS`
- [PullUpController](https://github.com/MarioIannotta/PullUpController) - Pull up controller with multiple sticky points like in iOS Maps.
- [shortcuts-drawer-view](https://github.com/phillfarrugia/shortcuts-drawer-view) - An experimental re-creation of Siri Shortcut's Drawer View component.
- [SlideOverCard](https://github.com/joogps/SlideOverCard) - A SwiftUI card design, similar to the one used by Apple in HomeKit, AirPods and Apple Card setup, NFC scanning, Wi-Fi password sharing and more. It is specially great for setup interactions. `iOS` `SwiftUI`
- [SOPullUpView](https://github.com/Ahmadalsofi/SOPullUpView) - SOPullUpView library for iOS, with pull up gesture.
- [SPStorkController](https://github.com/ivanvorobei/SPStorkController) - Now playing controller from Apple Music. Customisable height.
- [swiftui-drawer](https://github.com/maustinstar/swiftui-drawer) - A SwiftUI bottom-up controller, like in the Maps app. Drag to expand or minimize. `iOS` `macOS` `SwiftUI`
- [TopDrawer](https://github.com/JUSTINMKAUFMAN/TopDrawer) - A top drawer that can be pulled up/down over the screen.
- [UBottomSheet](https://github.com/OfTheWolf/UBottomSheet) - Bottom sheet that mimics the behaviours and UI of iPhone Maps app. `iOS`
- [VerticalSlidingPresentationController](https://github.com/liyu-wang/VerticalSlidingPresentationController)

### Routing and deep links

- [Appz](https://github.com/SwiftKitz/Appz) - Launch external apps, and deeplink, with ease using Swift! `iOS` `watchOS`
- [branch deep linking](https://github.com/BranchMetrics/ios-branch-deep-linking-attribution) - The Branch iOS SDK for deep linking and attribution. Branch helps mobile apps grow with deep links / deeplinks that power paid acquisition and re-engagement campaigns, referral programs, content sharing, deep linked emails, smart banners, custom user onboarding, and more.
- [Compass](https://github.com/hyperoslo/Compass) - Compass helps you setup a central navigation system for your application. `iOS`
- [Crossroad](https://github.com/giginet/Crossroad) - Crossroad
- [FeatherweightRouter](https://github.com/FeatherweightLabs/FeatherweightRouter) - Swift based Application State Router.
- [IKRouter](https://github.com/IanKeen/IKRouter) - URLScheme router than supports auto creation of UIViewControllers for associated url parameters to allow creation of navigation stacks.
- [RFShortURL](https://github.com/rfunk82/RFShortURL) - RFShortURL provides free URL redirection service.
- [route-composer](https://github.com/ekazaev/route-composer) - Protocol oriented, Cocoa UI abstractions based library that helps to handle view controllers composition, routing and deep linking tasks in the iOS application. `iOS`
- [Router](https://github.com/1amageek/Router) - Router is a library that assists with SwiftUI view transitions. `SwiftUI`
- [URLNavigator](https://github.com/devxoul/URLNavigator) - Elegant URL Routing for Swift. `iOS`
- [Wayfaring](https://github.com/terut/Wayfaring) - Routing library for Swift.
- [Yukina](https://github.com/charlesmwang/Yukina) - In App URL Router (Deep-Linking Framework for Swift).

### Sharing

- [VisualActivityViewController](https://github.com/naturaln0va/VisualActivityViewController) - A way to represent what you’re sharing. `iOS`

### Tab bars

- [Adaptive TabBar](https://github.com/Ramotion/adaptive-tab-bar) - AdaptiveController is a 'Progressive Reduction' Swift module for adding custom states to Native or Custom iOS UI elements. `iOS`
- [AHCategoryView](https://github.com/ivsall2012/AHCategoryView) - A navigation view for categories
- [AMPagerTabs](https://github.com/Abedalkareem/AMPagerTabs) - Pager tabs for iOS.
- [AMTabView](https://github.com/Abedalkareem/AMTabView) - AMTabView is a custom tab bar with amazing animation.
- [Animated-Tab-Bar](https://github.com/Ramotion/animated-tab-bar) - :octocat: RAMAnimatedTabBarController is a Swift UI module library for adding animation to iOS tabbar items and icons. iOS library made by @Ramotion `iOS`
- [AnimatedTabBar](https://github.com/AlbGarciam/AnimatedTabBar) - AnimatedTabBar is a Swift module library for adding animation to iOS tabBar items and icons. `iOS`
- [AnimateTabbarBadgeView](https://github.com/AliAdam/AnimateTabbarBadgeView) - UITabBarController Extention to make badge View animated.
- [AZTabBarController](https://github.com/Minitour/AZTabBarController) - A custom tab bar controller for iOS written in Swift 3.0.
- [bottombar-swiftui](https://github.com/smartvipere75/bottombar-swiftui) - BottomBar component for SwiftUI. `SwiftUI`
- [CircleBar](https://github.com/softhausHQ/CircleBar) - A fun, easy-to-use tab bar navigation controller for iOS.
- [ColorMatchTabs](https://github.com/Yalantis/ColorMatchTabs) - This is a Review posting app that let user find interesting places near them `iOS`
- [CustomTabBarShape](https://github.com/Monntay/CustomTabBarShape) - Draw a Custom iOS TabBar shape [tutorial](https://medium.com/better-programming/draw-a-custom-ios-tabbar-shape-27d298a7f4fa)
- [flashy-tabbar](https://github.com/Cuberto/flashy-tabbar) - One another nice animated tabbar.
- [FloatingTabBar](https://github.com/claudiaeng/FloatingTabBar) - Aesthetic floating tab bar. `iOS` `SwiftUI`
- [FredKitTabBarSplitView](https://github.com/riedel-wtf/FredKitTabBarSplitView) - A subclass of UITabBarController that translates UITabBarItems 1:1 into a Sidebar on iPadOS.
- [GooeyTabbar](https://github.com/KittenYang/GooeyTabbar) - A gooey effect tabbar.
- [HHTabBarView](https://github.com/hemangshah/HHTabBarView) - A lightweight customized tabbar view. `Archived`
- [JBTabBarAnimation](https://github.com/jithinpala/JBTabBarAnimation) - A custom TabBarController animation.
- [KPSmartTabBar](https://github.com/KrishnaPatell/KPSmartTabBar) - A fully customisable and flexible tab bar controller.
- [lightCardTabBar](https://github.com/hussc/lightCardTabBar) - An expiremental project exploring different types of custom-tabbar styles, screenshots as below.
- [LXPageViewWithButtonsViewController](https://github.com/lxian/LXPageViewWithButtonsViewController) - Combines UIPageViewController and highly customisable page selection tabs.
- [MHImageTabBar](https://github.com/mho000/MHImageTabBar) - UITabBarController Replacement
- [MightyTabBar](https://github.com/timshim/MightyTabBar) - MightyTabBar is a customizable tab bar that doubles as a menu drawer. Instead of being limited to 5 tab bar items, MightyTabBar allows your app to have many more tab bar items, all positioned within the thumb zone and easily accessible via swipe up. `iOS`
- [MiniTabBar](https://github.com/D-32/MiniTabBar) - A minimal tab bar alternative. `iOS`
- [MIPivotPageController](https://github.com/MarioIannotta/MIPivotPageController) - MIPivotPageController allows switching viewcontroller with an horizontal swipe. `Archived`
- [MMTabBarAnimation](https://github.com/MillmanY/MMTabBarAnimation) - Custom Animation on tabbar Item.
- [Parchment](https://github.com/rechsteiner/Parchment) - A paging view controller with a highly customizable menu. Built on UICollectionView, with support for custom layouts and infinite data source. `iOS` `SwiftUI`
- [PolioPager](https://github.com/YuigaWada/PolioPager) - A flexible tabBar library with search tab like SNKRS. Written in pure swift.
- [PTCardTabBar](https://github.com/hussc/PTCardTabBar) - Card-Style TabBarController for iOS. `Archived`
- [SabBar](https://github.com/macteo/SabBar) - Drop-in UITabBarController subclass that shows a sidebar with tabs based on trait collections.
- [ScrollPager](https://github.com/aryaxt/ScrollPager) - A scroll pager that displays a list of tabs (segments) and manages paging between given views
- [Segmentio](https://github.com/Yalantis/Segmentio) - Animated top/bottom segmented control written in Swift. `iOS`
- [SMSwipeableTabView](https://github.com/smahajan28/SMSwipeableTabView) - Swipeable Views with Tabs (Like Android SwipeView With Tabs Layout).
- [SOTabBar](https://github.com/Ahmadalsofi/SOTabBar) - Light way to add Fancy bottom bar. `iOS`
- [SRTabBarController](https://github.com/steve228uk/SRTabBarController) - A UITabBarController clone for OS X. `macOS`
- [STTabbar](https://github.com/11Shraddha/STTabbar) - A subclass on UITabbar that provides allows you to customize a shape of UITabbar with raised center button. You can change appearance of tabbar according to your needs. `iOS`
- [SwiftPages](https://github.com/GabrielAlva/SwiftPages) - A swift implementation of a swipe between pages layout, just like Instagram's toggle between views.
- [SwiftPrefs](https://github.com/emiscience/SwiftPrefs) - A Yosemite-only demo app showing a preferences window using Swift, storyboards and NSTabViewController. `macOS`
- [SwipeableTabBarController](https://github.com/marcosgriselli/SwipeableTabBarController) - UITabBarController with swipe interaction between its tabs. `iOS`
- [TabbarControllerHideable](https://github.com/ezefranca/TabbarControllerHideable) - A drop in UITabbarController with show and hide options.
- [Tabby](https://github.com/hyperoslo/Tabby) - A fancy tabbar.
- [TabDrawer](https://github.com/winslowdibona/TabDrawer) - TabDrawer is a customizable TabBar UI element that allows you to run a block of code upon TabBarItem selection, or display a customizable drawer.
- [TabPageViewController](https://github.com/EndouMari/TabPageViewController) - Paging view controller and scroll tab view. `iOS`
- [TiltedTabView](https://github.com/ian-mcdowell/TiltedTabView) - iOS control to replicate the tab switcher in Safari for iOS.
- [TransitionableTab](https://github.com/ParkGwangBeom/TransitionableTab) - TransitionableTab makes it easy to animate when switching between tab. `iOS`
- [TTabBarViewController](https://github.com/msalah1193/TTabBarViewController) - Custom UITabBarController class which draw line indicator with custom color above or below the selected tab bar item using 'selectionIndicatorImage' property on the UITabBar class. `iOS`
- [VBRRollingPit](https://github.com/v-braun/VBRRollingPit) - Simple, beatiful and interactive UITabBar. `iOS`
- [WBSegmentControl](https://github.com/xiongxiong/WBSegmentControl) - An easy to use, customizable segment control, can be used to show tabs.
- [WhatsNewKit](https://github.com/SvenTiigi/WhatsNewKit) - Showcase your awesome new app features. `iOS` `macOS` `SwiftUI`
- [WormTabStrip](https://github.com/EzimetYusup/WormTabStrip) - Worm TabStrip Android ViewPager for iOS written in Swift, built from other view controllers placed inside a scroll view. `iOS`
- [XLPagerTabStrip](https://github.com/xmartlabs/XLPagerTabStrip) - Android PagerTabStrip for iOS.

### Toolbars

- [ISHHoverBar](https://github.com/iosphere/ISHHoverBar) - A floating UIToolBar replacement as seen in the iOS10 Maps app, supporting both vertical and horizontal orientation.

## Animation and feedback

### Animations

- [15 Days of Animations in Swift](https://github.com/larrynatalicio/15DaysofAnimationsinSwift) - A project to learn animations.
- [AAViewAnimator](https://github.com/EngrAhsanAli/AAViewAnimator) - AAViewAnimator is a set of animations designed for UIView, UIButton, UIImageView with options in iOS, written in Swift.
- [Advance](https://github.com/timdonnelly/Advance) - A powerful animation framework for iOS. `iOS` `Archived`
- [Anima](https://github.com/satoshin21/Anima) - Anima is chainable Layer-Based Animation library for Swift5.
- [AnimateBlurRadius](https://github.com/fichek/AnimateBlurRadius) - An example of how to interactively animate blur radius on iOS 10.
- [AnimatedWaveView](https://github.com/j-wilkin/AnimatedWaveView) - An interactive wave animation view built in Swift.
- [AppleONE](https://github.com/darioGzlez/AppleONE) - SwiftUI recreation of Apple One enrolling view, adding a extra animation for the services icons. `SwiftUI`
- [ATScrollingNumbers](https://github.com/anooptomar1/ATScrollingNumbers) - Scrolling number control with circular progress.
- [awesome-ios-animation](https://github.com/onmyway133/awesome-ios-animation) - :umbrella: A collection of iOS animation repos `iOS`
- [BLEPrgressView](https://github.com/ymmtshny/BLEPrgressView) - I am making an animation view for Bluetooth connection.
- [Bubble](https://github.com/goldmoment/Bubble) - Inspired by Fruit Animation
- [ConfettiKit](https://github.com/gokulnair2001/ConfettiKit) - ConfettiKit is a custom framework used to add Confetti on your iOS/iPadOS projects. The kit provides variety of customisations inorder to design a confetti which matches your project's UI.
- [ConfettiSwiftUI](https://github.com/simibac/ConfettiSwiftUI) - SwiftUI Package for Configurable Confetti Animation 🎉 `SwiftUI`
- [ConfettiView](https://github.com/NSHipster/ConfettiView) - A view that emits confetti. `Archived`
- [ConfettiView](https://github.com/OrRon/ConfettiView) - Confetti View lets you create a magnificent confetti view in your app.
- [CPConfettiView](https://github.com/phuongvnc/CPConfettiView) - CPConfettiView is fun animation when user input keyword.
- [Dance](https://github.com/saoudrizwan/Dance) - A radical & elegant animation library built for iOS. `iOS`
- [DCExplosion](https://github.com/Tangdixi/DCExplosion) - Remove a view with explosion animation
- [DDViewSwitcher](https://github.com/DingdingKim/DDViewSwitcher) - With DDViewSwitcher, you can simply implement the effect of scrolling the view with just two lines. Like android TextSwitcher. `iOS`
- [DoneHud](https://github.com/beryu/DoneHUD) - Done animation on HUD.
- [Ease](https://github.com/roberthein/Ease) - Animate everything with Ease.
- [Easing](https://github.com/manuelCarlos/Easing) - A library that implements easing functions in Swift.
- [EasyAnimation](https://github.com/icanzilb/EasyAnimation) - Design and prototype UI, interaction, navigation, transition and animation for App Store ready Apps in Interface Builder with IBAnimatable.
- [ElasticTransition](https://github.com/lkzhao/ElasticTransition) - A UIKit custom transition that simulates an elastic drag. `UIKit`
- [Equinox](https://github.com/rlxone/Equinox) - Equinox is an application that allows you to create macOS native wallpapers. `macOS` `AppKit`
- [fireworks](https://github.com/tomkowz/fireworks) - Fireworks for UIView.
- [FlightAnimator](https://github.com/AntonTheDev/FlightAnimator) - Natural Blocks Based Core Animation Framework. `iOS` `tvOS`
- [FlipTheBlinds](https://github.com/joelconnects/FlipTheBlinds) - FlipTheBlinds is an animation transition that creates a venetian blinds domino effect.
- [Fluent](https://github.com/matthewcheok/Fluent) - Swift Animations made Easy.
- [FlyToCart](https://github.com/pratik-123/FlyToCart) - Product add to cart animation like Flying to cart.
- [Gagat](https://github.com/Boerworz/Gagat) - A delightful way to transition between visual styles in your iOS applications.
- [Gemini](https://github.com/shoheiyokoyama/Gemini) - Gemini is rich scroll based animation framework for iOS, written in Swift. `iOS`
- [IBAnimatable](https://github.com/IBAnimatable/IBAnimatable) - Design and prototype customized UI, interaction, navigation, transition and animation for App Store ready Apps in Interface Builder with IBAnimatable. `iOS` `UIKit`
- [ImageSwapper](https://github.com/tsarikovskiy/ImageSwapper) - Nice iOS animations for swapping images. In progress. `iOS`
- [ImageTransition](https://github.com/shtnkgm/ImageTransition) - Library for smooth animation of images during transitions. `iOS` `Archived`
- [Interpolate](https://github.com/marmelroy/Interpolate) - Swift interpolation for gesture-driven animations. `iOS`
- [JDAnimationKit](https://github.com/JellyDevelopment/JDAnimationKit) - Animate easy and with less code with Swift. `iOS`
- [JellyAnimationView](https://github.com/malt03/JellyAnimationView)
- [JingRound](https://github.com/isaced/JingRound/tree/swift) - A music playback view similar to jing.fm, supporting rotation and customizable parameters. 仿jing.fm的音乐播放视图，支持旋转和自定义参数。
- [KFWatchKitAnimations](https://github.com/kiavashfaisali/KFWatchKitAnimations) - KFWatchKitAnimations creates beautiful 60 FPS animations for  Watch by recording animations from the iOS. `watchOS`
- [LNInterpolation](https://github.com/LeoNatan/LNInterpolation) - An interpolation framework for Cocoa and Cocoa Touch. `Archived`
- [LockAnimationTest](https://github.com/warpling/LockAnimationTest) - The iPhone X lock animation …unlocked.
- [lottie](https://github.com/airbnb/lottie-ios) - An iOS library to natively render After Effects vector animations. `iOS`
- [MarchingLayer](https://github.com/cemolcay/MarchingLayer) - domly fills layer with sprites and move them in any direction and speed you want.
- [material-motion-swift](https://github.com/material-motion/material-motion-swift) - Reactive motion for iOS. `iOS` `Archived`
- [metal-fireworks](https://github.com/kjpgit/metal-fireworks) - Fireworks Graphics Demo (Swift, Metal, macOS) `macOS` `Archived`
- [Morph](https://github.com/gbammc/Morph) - A wrapper for CoreAnimation (Swift). `iOS`
- [Motion Machine](https://github.com/poetmountain/MotionMachine) - A powerful, elegant, and modular animation library for Swift.
- [MountainView](https://github.com/KyoheiG3/MountainView) - The animation curve looks like Mountain View.
- [MovingNumbersView](https://github.com/aunnnn/MovingNumbersView) - Moving numbers effect in SwiftUI. `SwiftUI`
- [MTPrivateTrainerAnimation](https://github.com/MartinRGB/MTPrivateTrainerAnimation) - A simple implement of my design(DEPRECATED)
- [MTRipple](https://github.com/manekdilip/MTRipple) - Repository for Ripple Effect. `iOS`
- [NaughtyImageView](https://github.com/kevinzhow/NaughtyImageView) - UIImageView Can Animate Sprite Image.
- [Pastel](https://github.com/cruisediary/Pastel) - Instagram like Gradient background animation.
- [PIRipple](https://github.com/pixel-ink/PIRipple) - Ripple Effect for iOS (swift)
- [PowerUpYourAnimations](https://github.com/icanzilb/PowerUpYourAnimations) - Sample code from talks on advanced animations.
- [Pulsator](https://github.com/shu223/Pulsator) - Pulse animation for iOS. `iOS`
- [RazzleDazzle](https://github.com/IFTTT/RazzleDazzle) - A simple keyframe-based animation framework for iOS, written in Swift. Perfect for scrolling app intros.
- [Reading-Animation](https://github.com/Mindinventory/Reading-Animation) - Cool Reading Animation in iOS written in Swift.
- [RimhTypingLetters](https://github.com/rimh/RimhTypingLetters) - A simple typing animation for UITextView and UILabel in Swift.
- [RubberBandEffect](https://github.com/Produkt/RubberBandEffect) - Recreating Apple’s rubber band effect in Swift
- [SAConfettiView](https://github.com/sudeepag/SAConfettiView) - Confetti! Who doesn't like confetti?
- [SaveTheDot](https://github.com/JakeLin/SaveTheDot) - A game developed using UIViewPropertyAnimator. `iOS`
- [SHTransition](https://github.com/iamshezad/SHTransition) - SHTransition is a Library for the transition between the views in a viewcontroller.
- [SimpleFlipView](https://github.com/javalnanda/SimpleFlipView) - ViewSwitcher container that helps to switch between two views with transition animation.
- [SnowFalling](https://github.com/pixyzehn/SnowFalling) - Snow Falling in Swift. `Archived`
- [SPPerspective](https://github.com/ivanvorobei/SPPerspective) - Animatable widgets from iOS 14. `UIKit`
- [Spring](https://github.com/MengTo/Spring) - A library to simplify iOS animations in Swift.
- [springdamping](https://github.com/mortenjust/springdamping) - Realtime experimentation with duration, spring and damping for UIView animations.
- [spruce-ios](https://github.com/willowtreeapps/spruce-ios) - Swift library for choreographing animations on the screen. `iOS`
- [SRFacebookAnimation](https://github.com/shamshiranees/SRFacebookAnimation) - Facebook live streaming emoji animation which can be fully customised.
- [Stellar](https://github.com/AugustRush/Stellar) - A fantastic Physical animation library for swift. `iOS`
- [SwiftAnimations](https://github.com/AbsolutRenal/SwiftAnimations) - Try CALayer Animations in Swift.
- [SwiftUI-Animation](https://github.com/Arvindcs/SwiftUI-Animation) - SwiftUI Animation `SwiftUI`
- [UIViewXXYBoom](https://github.com/xxycode/UIViewXXYBoom) - A fun effect
- [UIWaveView](https://github.com/bionelabs/UIWaveView) - UIWaveView for app which show battery charging progress or something else. `iOS`
- [WVCheckMark](https://github.com/wvabrinskas/WVCheckMark) - Animated checkmark made with CoreAnimation.
- [WWDC-2017-Session-230-Advance-Animations-with-UIKit](https://github.com/cgoldsby/WWDC-2017-Session-230-Advance-Animations-with-UIKit) - Example project for "Sam's Photo" animations demonstrated in Session 203 `UIKit`

### Loading indicators

- [AALoaders](https://github.com/EngrAhsanAli/AALoaders) - AALoaders is a lightweight, easy-to-use and powerful progress view loaders framework, written in Swift. It uses simple native elements for progress loading with customisations and allow to use without creating instance.
- [AJProgressView](https://github.com/arpitjain03/AJProgressView) - A subclass of UIView for managing progress, which can be customized according to your application design.
- [BmoImageLoader](https://github.com/tzef/BmoImageLoader) - BmoImageLoader is a progress animated component for UIImageView.
- [BPBlockActivityIndicator](https://github.com/ppth0608/BPBlockActivityIndicator) - A simple and awesome loading Activity Indicator(with block moving animation) for your iOS app.
- [BPCircleActivityIndicator](https://github.com/ppth0608/BPCircleActivityIndicator) - A lightweight and awesome loading Activity Indicator for your iOS app. `iOS`
- [BRCircularProgressBar](https://github.com/BrammanandSoni/BRCircularProgressBar) - It shows circular progress for multi purpose like download, upload and timer progress.
- [CircleSlider](https://github.com/shushutochako/CircleSlider) - CircleSlider is a Circular slider library. written in pure Swift.
- [Dots](https://github.com/makomori/Dots) - Modern loading indicator for iOS 10.
- [DotsLoader](https://github.com/mattlawer/DotsLoader) - Dots Activity Indicator using Interface Builder.
- [DPBasicLoading](https://github.com/dwipp/DPBasicLoading) - It's a very basic loading in iOS.
- [DRPLoadingSpinner](https://github.com/justindhill/DRPLoadingSpinner) - A customizable loading spinner and refresh control for iOS that's strikingly Material-like.
- [DTIActivityIndicatorView-Swift](https://github.com/dtissera/DTIActivityIndicatorView-Swift) - Animated custom ActivityIndicator inspired from css library SpinKit and much more. Written in Swift.
- [EatFit](https://github.com/Yalantis/EatFit) - Eat fit is a component for attractive data representation inspired by Google Fit. `iOS`
- [FillableLoaders](https://github.com/polqf/FillableLoaders) - Completely customizable progress based loaders drawn using custom CGPaths written in Swift.
- [FliudLoadingIndicator](https://github.com/vinit5320/FliudLoadingIndicator) - Guide: https://swiftyos.wordpress.com/2015/08/02/animated-loading-indicator-swift-bafluidview/
- [Fluky](https://github.com/pedrommcarrasco/Fluky) - Loading based on random icons.
- [GradientLoadingBar](https://github.com/fxm90/GradientLoadingBar) - A customizable animated gradient loading bar. `iOS`
- [HexLoader](https://github.com/Kesava-Jawaharlal/HexLoader) - This is a open source library which shows a hexagon shaped loading indictor, developed CAShapeLayer and CABasicAnimation.
- [InstagramActivityIndicator](https://github.com/jmmanos/InstagramActivityIndicator) - Activity Indicator similar to Instagram's. `iOS` `UIKit`
- [ITActivityIndicator](https://github.com/iluuu1994/ITActivityIndicator) - A very simple alternative to UIActivityIndicatorView.
- [JBWatchActivityIndicator](https://github.com/mikeswanson/JBWatchActivityIndicator) - JBWatchActivityIndicator - An easy way to generate activity indicator images for Apple Watch. `watchOS`
- [JDGamesLoading](https://github.com/jamesdouble/JDGamesLoading) - Let User Play Game When Loading.
- [JDProgressRoundView](https://github.com/jamesdouble/JDProgressRoundView) - JDProgressRoundView is Stylish Process Meter Based on UIProgressView. It growns 5% every tap, or you can just set the progress u want.
- [KDCircularProgress](https://github.com/kaandedeoglu/KDCircularProgress) - A circular progress view with gradients written in Swift.
- [KOActivityIndicator](https://github.com/kohtenko/KOActivityIndicator) - Easy styled, IBDesigneble and IBInspectable activity indicator on swift
- [KoalaActivityIndicator](https://github.com/Rajaikumar-iOSDev/KoalaActivityIndicator) - 🐨 KoalaActivityIndicator is created for people who loves koala and wants to add a non boring version of activity indicator. `iOS`
- [KRActivityIndicatorView](https://github.com/Henryforce/KRActivityIndicatorView) - An activity indicator view for OSX written in Swift. `macOS`
- [KVSpinnerView](https://github.com/kuznetsovVladislav/KVSpinnerView) - KVSpinnerView is highly customizable progress HUD. `iOS`
- [Loader](https://github.com/samhann/Loader.swift) - This library allows you to easily add an FB style animated loading placeholder to your tableviews or collection views.
- [MAActivityIndicator](https://github.com/micazeve/MAActivityIndicator) - Dot activity indicator
- [MaterialLoadingIndicator](https://github.com/Tueno/MaterialLoadingIndicator) - Material like loading indicator sample for iOS. `iOS`
- [MediumProgressView](https://github.com/pixyzehn/MediumProgressView) - A progress view based on Medium web app. `SwiftUI` `Archived`
- [MFLFillableTextLoader](https://github.com/MattFoley/MFLFillableTextLoader) - Loading slash progress indicator based on filling stroked text.
- [MilestoneProgressView](https://github.com/pratikg29/MilestoneProgressView) - Created Milestone progressView in SwiftUI. Provide all custom controls to personalise it. `SwiftUI`
- [MKMagneticProgress](https://github.com/malkouz/MKMagneticProgress) - A circular progress bar for iOS written in Swift.
- [MOOverWatchLoadingView](https://github.com/minsOne/MOOverWatchLoadingView) - Animation like OverWatch Loading written in Swift.
- [navigationLoader](https://github.com/nickypatson/NavigationLoader) - Simple Navigation Loader.
- [NKWatchActivityIndicator](https://github.com/NilStack/NKWatchActivityIndicator) - An activity indicator library for Apple Watch and a sample to push the limit of animation in watchOS 2. `watchOS`
- [NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView) - A collection of awesome loading animations `iOS`
- [ParticlesLoadingView](https://github.com/BalestraPatrick/ParticlesLoadingView) - A customizable SpriteKit particles animation on the border of a view. `iOS`
- [Pie-Progress-View](https://github.com/152percent/Pie-Progress-View) - A progress view – represented by a pie chart – to demonstrate how to make a Core Animation backed view/layer with support for both iOS and macOS. `macOS`
- [ProgressButton](https://github.com/alkhokhlov/ProgressButton) - Custom ProgressButton.
- [ProgressKit](https://github.com/kaunteya/ProgressKit) - Progress Views for OSX. `macOS` `Archived`
- [ProgressMaskView](https://github.com/eytyet/ProgressMaskView) - Progress view which masks the entire screen.
- [RSDotsView](https://github.com/remstos/RSDotsView) - A simple view that show pulsing dots
- [SegmentedProgressView](https://github.com/iSapozhnik/SegmentedProgressView) - Simple Instagram-like segmented progress view with completion handler and different time interval for each segment. `iOS`
- [SemiCircular-Scale](https://github.com/ankits16/SemiCircular-Scale) - A simple component to show circular scale, gauge etc.
- [SwiftOverlays](https://github.com/peterprokop/SwiftOverlays) - A Swift GUI library for displaying various popups and notifications `iOS`
- [SwiftSpinner](https://github.com/icanzilb/SwiftSpinner) - A beautiful activity indicator and modal alert written in Swift (originally developed for my app DoodleDoodle) Using blur effects, translucency, flat and bold design - all iOS 8 latest and greatest
- [UICircularProgressRing](https://github.com/luispadron/UICircularProgressRing) - A circular progress bar for iOS written in Swift 3. `iOS` `Archived`
- [VerticalProgressScrollView](https://github.com/VamshiIITBHU14/VerticalProgressScrollView) - This is a simple project showing UIScrollView with paging enabled and a straight forward Vertical Progress bar which animates as the user scrolls through the pages (number of pages are calculated dynamically based on content size). Written in latest Swift Syntax.

### Physics and dynamics

- [Newtons-Cradle](https://github.com/bishalg/Newtons-Cradle) - Newtons Cradle - Bearing in Swift using UIDynamicBehavior.
- [PhysicsCup](https://github.com/jnfisher/PhysicsCup) - iOS Sprite Kit demonstration in Swift

### Progress indicators

- [CircularProgress](https://github.com/sindresorhus/CircularProgress) - Circular progress indicator for your macOS app. `macOS`
- [Download-Indicator](https://github.com/MaheshRS/Download-Indicator) - This is a iOS Download Indicator for iOS 7, which can be used for showing the download % of the files being downloaded.
- [GradientCircularProgress](https://github.com/keygx/GradientCircularProgress) - Customizable progress indicator library in Swift `iOS`
- [GradientProgressBar](https://github.com/fxm90/GradientProgressBar) - A customizable gradient progress bar (UIProgressView). `iOS`
- [GTProgressBar](https://github.com/gregttn/GTProgressBar) - Customisable progress bar written in Swift 3.
- [JCGGProgressBar](https://github.com/jacquesCedric/JCGGProgressBar) - macOS custom progress bar UI component. `macOS`
- [KDLoadingView](https://github.com/KaiqueDamato/KDLoadingView) - A beautiful loading indicator. Written in Swift.
- [KYCircularProgress](https://github.com/kentya6/KYCircularProgress) - Flexible progress bar written in Swift.
- [MHProgressButton](https://github.com/emadhegab/MHProgressButton) - See the loading progress on your UIButton.
- [MultiProgressView](https://github.com/mac-gallagher/MultiProgressView) - MultiProgressView is an animatable view that depicts multiple progresses over time. Modeled after UIProgressView. `iOS`
- [OGCircularBar](https://github.com/OskarGroth/OGCircularBar) - Circular progress bar for macOS. `macOS`
- [SRCountdownTimer](https://github.com/rsrbk/SRCountdownTimer) - This is the simple circle countdown with a configurable timer for iOS.
- [tripleBar-swift](https://github.com/Ku6ep/tripleBar-swift) - Swift arc triple progress bar.
- [TYProgressBar](https://github.com/yashthaker7/TYProgressBar) - Custom animating gradient progress bar. `iOS`

### View controller transitions

- [AAPopUp](https://github.com/EngrAhsanAli/AAPopUp) - AAPopUp is a simple and easy-to-use popup view controller designed to present customizable storyboard based view controller as a modal alert, written in Swift..
- [AICustomViewControllerTransition](https://github.com/cocoatoucher/AICustomViewControllerTransition) - Easy and tidy way for creating custom UIViewController transitions for iOS.
- [animation-transition-viewcontroller-advanced](https://github.com/franobarrio/animation-transition-viewcontroller-advanced) - [Tutorial](https://medium.com/flawless-app-stories/cool-custom-view-controller-transitions-advanced-df2d0ca08029)
- [AZTransitions](https://github.com/azimin/AZTransitions) - API to make great custom transitions in one method.
- [CardPresentationController](https://github.com/radianttap/CardPresentationController) - Custom UIPresentationController which mimics the behavior of Apple Music UI. `UIKit` `Archived`
- [CardTransitionWithViewControllers-Example](https://github.com/wibosco/CardTransitionWithViewControllers-Example) - An example project looking at producing a view transition similar to the App Store card transition by using child view controllers. `iOS`
- [CustomSegue](https://github.com/phimage/CustomSegue) - Custom segue for OSX Storyboards with slide and cross fade effects (NSViewControllerTransitionOptions). `macOS`
- [DAExpandAnimation](https://github.com/ifitdoesntwork/DAExpandAnimation) - A custom modal transition that presents a controller with an expanding effect while sliding out the presenter remnants. `iOS` `UIKit`
- [EasyTransitions](https://github.com/marcosgriselli/EasyTransitions) - A simple way to create custom interactive UIViewController transitions. `iOS`
- [Elastic](https://github.com/lkzhao/Elastic) - Fancy elastic transition powered by Metal, UIKit Dynamics, & Hero. `UIKit`
- [FluidInterfaceKit](https://github.com/FluidGroup/FluidInterfaceKit) - FluidInterfaceKit provides the advanced infrastructure for your iPhone apps. `iOS` `UIKit`
- [Hero](https://github.com/HeroTransitions/Hero) - Supercharged transition engine for iOS. `iOS`
- [ImageOpenTransition](https://github.com/mcmatan/ImageOpenTransition) - Beautiful and precise transitions between ViewControllers images written in Swift.
- [inbox-replica](https://github.com/miralem-cebic/inbox-replica) - Recreated the expanding cells effect from `Inbox` by Google in Swift. `Archived`
- [ISScrollViewPageSwift](https://github.com/Ilhasoft/ISScrollViewPageSwift) - ScollView with UIViewController. `Archived`
- [Kaeru](https://github.com/bannzai/Kaeru) - Kaeru can switch ViewController in NavigationController like iOS task manager UI (after iOS 9).
- [KMNavigationBarTransition](https://github.com/MoZhouqi/KMNavigationBarTransition) - A drop-in universal library helps you to manage the navigation bar styles and makes transition animations smooth between different navigation bar styles while pushing or popping a view controller for all orientations.
- [MMTransition](https://github.com/MillmanY/MMTransition) - Custom UIPresentationController with (menu/dialog).
- [Motion](https://github.com/CosmicMind/Motion) - Seamless animations and transitions in Swift. `iOS`
- [Movin](https://github.com/xxxAIRINxxx/Movin) - UIViewPropertyAnimator based View Transition Animator.
- [MusicPlayerTransition](https://github.com/xxxAIRINxxx/MusicPlayerTransition) - Custom interactive transition like Apple Music iOS App (iOS 9). written in Swift.
- [PerfectContributionsView](https://github.com/jjunhaa0211/PerfectContributionsView) - 🌳 Library created to create GitHub contributions 🌲 `iOS`
- [Presentr](https://github.com/IcaliaLabs/Presentr) - Wrapper for custom ViewController presentations in iOS 8+. `iOS`
- [PullToDismiss](https://github.com/sgr-ksmt/PullToDismiss) - Dismiss ViewController by pulling scroll view or navigation bar in Swift. `iOS`
- [QZCircleSegue](https://github.com/alextarrago/QZCircleSegue) -  Beatiful transition between circular-shapped buttons and your View Controller.
- [RadialTransition_swift](https://github.com/apadalko/RadialTransition_swift) - Great iOS radial (circle) animation transition for navigation controller, with custom back swipe. (swift)
- [RDGliderViewController-Swift](https://github.com/gelemias/RDGliderViewController-Swift) - Control for a floating view gliding over a ViewController Edit.
- [RetroTransition](https://github.com/wcgray/RetroTransition) - Fun implementations of UIViewControllerAnimatedTransitioning for 90s inspired transitions between view controllers.
- [SamuraiTransition](https://github.com/hachinobu/SamuraiTransition) - a ViewController transition framework in Swift.
- [SPLarkController](https://github.com/ivanvorobei/SPLarkController) - Transition between controllers to top.
- [SpotifyPlayer](https://github.com/sgl0v/SpotifyPlayer) - This is the demo project of the article written in my blog. It shows how to create interactive animations using UIViewPropertyAnimator.
- [StatefulViewController](https://github.com/aschuch/StatefulViewController) - Placeholder views based on content, loading, error or empty states.
- [SwiftPagingNav](https://github.com/aubrey/SwiftPagingNav) - A Twitter-like navigation bar and page viewer written in Swift.
- [SwipeTransition](https://github.com/tattn/SwipeTransition) - Allows trendy transitions using swipe gesture such as "swipe back". `iOS`
- [Transition](https://github.com/Touchwonders/Transition) - Easy interactive interruptible custom ViewController transitions. `iOS`
- [TransitionController](https://github.com/pikachu987/TransitionController) - You can dismiss transition and present transition between UIViewController, UINavigationController, UITabBarController, UICollectionViewController, and UITableViewController.
- [TransitionManager](https://github.com/cemolcay/TransitionManager) - Painless custom transitioning. Easy extend, easy setup, just focus on animations.
- [View2ViewTransition](https://github.com/naru-jpn/View2ViewTransition) - Custom interactive view controller transition from one view to another view.
- [ViewAnimator](https://github.com/marcosgriselli/ViewAnimator) - ViewAnimator is a library for building complex iOS UIView animations in an easy way. It provides one line animations for any view included the ones which contain other views like UITableView and UICollectionView with its cells or UIStackView with its arrangedSubviews. `iOS` `UIKit`
- [ViewControllerPresentation](https://github.com/an0/ViewControllerPresentation) - Playground for trying out all presentation styles. Seeing them live gives a much better understanding than reading the documentation. `iOS`
- [VLCircularTransition](https://github.com/Vigneshlakshminarayanan/VLCircularTransition) - Circular ViewController Transition - Replacement to Apple's boring Push/Present Transitions.
- [ZoomTransitioning](https://github.com/WorldDownTown/ZoomTransitioning) - ZoomTransitioning provides a custom transition with image zooming animation. `iOS`

## Graphics and typography

### Charts

- [3DGraph](https://github.com/greglecki/3DGraph) - An interactive Swift 3D Graph.
- [AAChartKit-Swift](https://github.com/AAChartModel/AAChartKit-Swift) - An elegant and friendly chart library for iOS developer who use Swift. `iOS`
- [AnimatedGraph](https://github.com/alkhokhlov/AnimatedGraph) - Animated Graph which you can include in your application to show information in more attractive way.
- [APLineChart](https://github.com/tylyo/APLineChart) - IOS Line Chart
- [Attabench](https://github.com/attaswift/Attabench) - Microbenchmarking app for Swift with nice log-log plots. `macOS`
- [BarChart](https://github.com/romanbaitaliuk/BarChart) - Lightweight and easy to use SwiftUI chart library for all Apple platforms. `iOS` `macOS` `watchOS` `SwiftUI`
- [BarChart](https://github.com/nhatminh12369/BarChart) - This code demonstrate a way to build your own bar chart without using any third-party library. I don't recommend you to import BasicBarChart.swift and BeautifulBarChart.swift directly into your project. However, you should modify it according to your needs.
- [ChartLegends](https://github.com/ivnsch/ChartLegends) - Convenient and flexible legends for all kind of charts. `iOS`
- [ChartView](https://github.com/AppPear/ChartView) - ChartView made in SwiftUI. `iOS` `SwiftUI`
- [CoreCharts](https://github.com/cagricolak/CoreCharts) - CoreCharts is a simple powerfull yet Charts library for apple products. `iOS`
- [CSPieChart](https://github.com/youkchansim/CSPieChart) - This is pie chart that is very easy to use and customizable design.
- [DSFSparkline](https://github.com/dagronf/DSFSparkline) - A lightweight sparkline component, supporting Swift, SwiftUI, macCatalyst and Objective-C. `iOS` `macOS` `tvOS` `SwiftUI` `UIKit` `AppKit`
- [HeartRate](https://github.com/LiMaoAtCD/HeartRate) - Chart for Decibel.
- [HSStockChart](https://github.com/zyphs21/HSStockChart) - Stock Chart include CandleStickChart,TimeLineChart.
- [ILG](https://github.com/joeynelson42/ILG) - because the world needs another iOS chart library. `iOS`
- [ios-charts](https://github.com/ChartsOrg/Charts) - Beautiful charts for iOS/tvOS/OSX.
- [LineChart](https://github.com/nhatminh12369/LineChart) - A light-weight line chart for iOS. Swift 5.0, XCode 10.2
- [mobile-analytics-chart-swift](https://github.com/yoomoney/mobile-analytics-chart-swift) - This library allows implementing charts into mobile apps `iOS` `Archived`
- [OMScrollableChart](https://github.com/jaouahbi/OMScrollableChart) - An adaptive scrollable chart for iOS to visualise simple discrete datasets.
- [PieCharts](https://github.com/ivnsch/PieCharts) - Easy to use and highly customizable pie charts library for iOS. `iOS`
- [PNChart-Swift](https://github.com/kevinzhow/PNChart-Swift) - A simple and beautiful chart lib used in Piner and CoinsMan for iOS(https://github.com/kevinzhow/PNChart) Swift Implementation
- [RadarChartView](https://github.com/furuyan/RadarChartView) - RadarChart for iOS. `iOS`
- [RHLinePlot](https://github.com/aunnnn/RHLinePlot) - Line plot like in Robinhood app, in SwiftUI. `SwiftUI`
- [ROStorageBar](https://github.com/prine/ROStorageBar) - Dynamic Storage Bar (a là iTunes Usage Bar) written in Swift
- [ScrollableGraphView](https://github.com/philackm/ScrollableGraphView) - An adaptive scrollable graph view for iOS to visualise simple discrete datasets. Written in Swift.
- [SpreadsheetView](https://github.com/kishikawakatsumi/SpreadsheetView) - Full configurable spreadsheet view user interfaces for iOS applications. With this framework, you can easily create complex layouts like schedule, gantt chart or timetable as if you are using Excel.
- [StackViewBarChart](https://github.com/haojianzong/StackViewBarChart) - A simple yet beautiful bar chart view for iOS powered by UIStackView. Written in Swift.
- [swift-linechart](https://github.com/zemirco/swift-linechart) - SwiftUI library to easily render diagrams given a tree of objects. Similar to ring chart, sunburst chart, multilevel pie chart. `SwiftUI`
- [SwiftCharts](https://github.com/ivnsch/SwiftCharts) - Easy to use and highly customizable charts library for iOS `iOS`
- [swiftplot](https://github.com/KarthikRIyer/swiftplot) - Swift library for Data Visualization.
- [SwiftSunburstDiagram](https://github.com/lludo/SwiftSunburstDiagram) - SwiftUI library to easily render diagrams given a tree of objects. Similar to ring chart, sunburst chart, multilevel pie chart. `iOS` `macOS` `SwiftUI`
- [SwiftUICharts](https://github.com/willdale/SwiftUICharts) - A charts / plotting library for SwiftUI. Works on macOS, iOS, watchOS, and tvOS. `iOS` `macOS` `tvOS` `SwiftUI`
- [WYChart](https://github.com/GeorgeWang03/WYChart) - A simple and elegant Chart library with rich animations.

### Colors

- [BCColor](https://github.com/boycechang/BCColor) - A lightweight but powerful color kit (Swift).
- [clrex](https://github.com/ilyapuchka/clrex) - Simple script to generate UIColor factory methods from clr files.
- [Color-Picker-for-iOS](https://github.com/hayashi311/Color-Picker-for-iOS) - Colorful: iOS color picker built with Swift. `iOS` `UIKit`
- [Colorblinds](https://github.com/jdekock/Colorblinds) - Colorblinds is an easy to use library so simulate color blindness in your app.
- [Colors](https://github.com/paulot/Colors) - Terminal Colors for Swift.
- [DPTheme](https://github.com/dphans/DPTheme) - DPTheme help you set default theme color for your app.
- [DynamicColor](https://github.com/yannickl/DynamicColor) - DynamicColor provides powerful methods to manipulate colours in an easy way. `SwiftUI`
- [flatuicolor](https://github.com/avdyushin/FlatUIColor) - Flat UIColor swift extenstion
- [himbo](https://github.com/DK1DA/Himbo) - A simple iOS App to create mono colored backgrounds. Written in Swift and supporting 3D Touch on iPhone 6s.
- [Hue](https://github.com/zenangst/Hue) - Hue is the all-in-one coloring utility that you'll ever need.
- [IVColorPicker](https://github.com/irilka/IVColorPicker)
- [JMCRainbow](https://github.com/gulfcoastdev/JMCRainbow) - UIView extension for generating 'rainbow' background.
- [MaterialKit](https://github.com/nghialv/MaterialKit) - Material design components for iOS written in Swift.
- [Palette](https://github.com/galandezzz/Palette) - Color palette generation from image written in Swift.
- [PixColor](https://github.com/chuongtrh/PixColor) - Generate palette color from image.
- [PrettyColors](https://github.com/jdhealy/PrettyColors) - PrettyColors is a Swift library for styling and coloring text in the Terminal. The library outputs ANSI escape codes and conforms to ECMA Standard 48.
- [ProtocolUI](https://github.com/VojtaStavik/ProtocolUI) - ProtocolUI is a simple helper file providing very basic infrastructure for customizing UI elements via protocol extensions.
- [UIColor-Hex-Swift](https://github.com/yeahdongcn/UIColor-Hex-Swift) - Convenience method for creating autoreleased color using RGBA hex string.
- [UIImageColors](https://github.com/jathu/UIImageColors) - iTunes style color fetcher for UIImage. `iOS` `Archived`

### Fonts and icons

- [AVFonts](https://github.com/arnavgupta180/AVFonts) - AVFonts for change/swap fontname throughout app.
- [Font-Awesome-Swift](https://github.com/thii/FontAwesome.swift) - Use FontAwesome in your Swift projects `iOS` `macOS` `tvOS`
- [Fontawesome](https://github.com/hirohisa/Font-Awesome) - Demonstrates how to download fonts on demand on iOS 6 and later.
- [FontBlaster](https://github.com/ArtSabintsev/FontBlaster) - Say goodbye to importing custom fonts via property lists as FontBlaster automatically imports and loads all fonts in your app's NSBundles with one line of code. `tvOS`
- [GoogleMaterialIconFont](https://github.com/kitasuke/GoogleMaterialIconFont) - Google Material Design Icons for Swift and ObjC project.
- [Iconic](https://github.com/home-assistant/Iconic) - Auto-generated icon font library for iOS & tvOS. `iOS` `tvOS` `watchOS` `Archived`
- [MaterialDesignSymbol](https://github.com/tichise/MaterialDesignSymbol) - Icon font library for Swift. Currently supports GoogleMaterialDesignIcons `SwiftUI`
- [MBIcons](https://github.com/c-Viorel/MBIcons) - MBIcons contains over 100 icons that can be resized to any dimensions as they are drawn using NSBezierPath. `macOS`
- [SFSafeSymbols](https://github.com/SFSafeSymbols/SFSafeSymbols) - A safe way to access Apple's SF System Symbols using static typing. `iOS`
- [SwiftFontName](https://github.com/morizotter/SwiftFontName) - OS font complements library. Localized font supported. `Archived`
- [UIFontComplete](https://github.com/Nirma/UIFontComplete) - Make working with UIFont faster and less error-prone.

### Geometry and drawing

- [CubicEquationSolver](https://github.com/dnpp73/CubicEquationSolver) - Cubic Equation Solver written in Swift for iOS, macOS.
- [Decomposed](https://github.com/b3ll/Decomposed) - Decomposed makes CATransform3D, matrix_double4x4, and matrix_float4x4 much easier to work with. `iOS` `macOS`
- [Euclid](https://github.com/nicklockwood/Euclid) - A Swift library for creating and manipulating 3D geometry
- [InkKit](https://github.com/shaps80/InkKit) - Drawing and Geometry made easy for iOS. `iOS`
- [Macaw](https://github.com/exyte/Macaw) - Powerful and easy-to-use vector graphics Swift library with SVG support. `iOS`
- [SwiftCGRectExtensions](https://github.com/nschum/SwiftCGRectExtensions) - A collection of CGRect, CGPoint and CGSize convenience functions for Swift.

### Labels

- [ActiveLabel](https://github.com/optonaut/ActiveLabel.swift) - UILabel drop-in replacement supporting Hashtags (#), Mentions (@) and URLs (http://) written in Swift.
- [AGTypewriterLabel](https://github.com/aivantg/AGTypewriterLabel) - Simple UILabel that displays text character by character as it would be typed by a typewriter.
- [ASAttributedLabelNode](https://github.com/alex-alex/ASAttributedLabelNode) - Draw NSAttributedString in SpriteKit
- [EFAutoScrollLabel](https://github.com/EFPrefix/EFAutoScrollLabel) - A label which can scroll when text length beyond the width of label. `iOS`
- [FlashingLabel](https://github.com/dokgi88/FlashingLabel) - Veeeeeeeeeeeeeeeery easy to use and simple Flashing Label.
- [GlitchLabel](https://github.com/kciter/GlitchLabel) - glitch effect
- [GlowingLabel](https://github.com/RajChanchal/GlowingLabel) - A label with an outer glow.
- [GranibleLabel](https://github.com/dokgi88/GranibleLabel) - Veeeeeeeeeeeeeeeery easy to use and simple gradation animate Label.
- [IHTypeWriterLabel](https://github.com/Ibrahimhass/IHTypeWriterLabel) - A simple, UILabel subclass which poulates itself as if being typed. `iOS`
- [IncrementableLabel](https://github.com/tbaranes/IncrementableLabel) - IncrementableLabel is the easiest way to have incrementable numbers in an UILabel!.
- [KDEDateLabel](https://github.com/delannoyk/KDEDateLabel) - UILabel subclass that saves you from refreshing it when using 'time ago' format.
- [LoadingShimmer](https://github.com/jogendra/LoadingShimmer) - An easy way to add a shimmering effect to any view with just one line of code. It is useful as an unobtrusive loading indicator. `iOS`
- [LTMorphingLabel](https://github.com/lexrus/LTMorphingLabel) - Graceful morphing effects for UILabel written in Swift.
- [MAGlowingLabel](https://github.com/Marwan8/MAGlowingLabel) - A UILabel with an animated glowing effect written in Swift.
- [MarqueeLabel](https://github.com/cbpowell/MarqueeLabel) - A drop-in replacement for UILabel, which automatically adds a scrolling marquee effect when the label's text will not fit inside the specified frame. `iOS`
- [MarqueeText](https://github.com/joekndy/MarqueeText) - A SwiftUI Marquee or "scrolling text" effect found in Apple native apps. `SwiftUI`
- [Nantes](https://github.com/instacart/Nantes) - TTTAttributedLabel replacement. `iOS`
- [NumberMorphView](https://github.com/me-abhinav/NumberMorphView) - A label view for displaying numbers which can transition or animate using a technique called number tweening or number morphing.
- [NumericAnimatedLabel](https://github.com/javalnanda/NumericAnimatedLabel) - Animate numeric value while setting new value to label.
- [ODMultiColumnLabel](https://github.com/Sephiroth87/ODMultiColumnLabel) - A UILabel replacement that renders text on multiple columns.
- [SwiftyScrollingLabel](https://github.com/Sahilberi/SwiftyScrollingLabel) - SwiftScrollingLabel is a subclass of UIView and it adds a label on it with scrolling marquee effect.

### Text and rich text

- [AnimatedField](https://github.com/alberdev/AnimatedField) - Animated UITextField with check & filter for default types (email, url, password, price, date...) for iOS.
- [AOR](https://github.com/xxxAIRINxxx/AOR) - Wrapper of NSAttributedString and Text Kit. written in Swift.
- [AttributedTextView](https://github.com/evermeer/AttributedTextView) - Easiest way to create an attributed UITextView with support for multiple links.
- [BezierString](https://github.com/lvnyk/BezierString) - Rendering NSAttributedStrings along arbitrary UIBezierPaths.
- [BonMot](https://github.com/Rightpoint/BonMot) - Beautiful, easy attributed strings for iOS.
- [CodeEditor](https://github.com/ZeeZide/CodeEditor) - A SwiftUI TextEditor View with syntax highlighting using Highlight.js. `SwiftUI`
- [Down](https://github.com/johnxnguyen/Down) - Blazing fast Markdown rendering in Swift, built upon cmark. `iOS` `macOS` `tvOS`
- [DPTagTextView](https://github.com/Datt1994/DPTagTextView) - Add & detect tag/mention using Textview.
- [EmojiTextView](https://github.com/fastred/EmojiTextView) - Tap to swap out words with emojis. Inspired by Messages.app on iOS 10. `Archived`
- [GrowingTextView](https://github.com/KennethTsang/GrowingTextView) - An UITextView in Swift. Support auto growing, placeholder and length limit.
- [HandyText](https://github.com/aleksey-ios-dev/HandyText) - HandyText is a helper library that allows to create and manage text styles in a clear declarative manner.
- [Highlighter](https://github.com/younatics/Highlighter) - Highlight whatever you want! Highlighter will magically find UI objects such as UILabel, UITextView, UITexTfield, UIButton in your UITableViewCell or other Class.
- [HighlightTextView](https://github.com/yusayusa/HighlightTextView)
- [input-mask-ios](https://github.com/RedMadRobot/input-mask-ios) - User input masking library repo. `iOS`
- [JSONPreview](https://github.com/RakuyoKit/JSONPreview) - A view that can be highlighted after formatting JSON. `iOS`
- [MarkdownView](https://github.com/keitaoouchi/MarkdownView) - Markdown View for iOS. `iOS`
- [Marklight](https://github.com/macteo/Marklight) - Markdown syntax highlighter for iOS.
- [Markup](https://github.com/gonzalezreal/Markup) - Lightweight markup text formatting in Swift. `iOS` `macOS` `tvOS`
- [Mustard](https://github.com/mathewsanders/Mustard) - Mustard is a Swift library for tokenizing strings when splitting by whitespace doesn't cut it.
- [NextGrowingTextView](https://github.com/FluidGroup/NextGrowingTextView) - The next in the generations of 'growing textviews' optimized for iOS 7 and above. `iOS`
- [NSJFontResizingUITextView](https://github.com/NSJoker/NSJFontResizingUITextView) - UITextField adjusts its font size dynamicaly with respect to is content. `iOS`
- [PlaceholderUITextView](https://github.com/hoangtaiki/PlaceholderUITextView) - A missing placeholder for UITextView. `UIKit`
- [PTPPlaceholderTextView](https://github.com/pitiphong-p/PTPPlaceholderTextView) - A simple naive implementation of UITextView subclass to support placeholder text rendering in UITextView.
- [RaisePlaceholder](https://github.com/najanda89/RaisePlaceholder)
- [RealtimeGradientText](https://github.com/kevinzhow/RealtimeGradientText) - Gradient Text in Real.
- [Reductio](https://github.com/fdzsergio/Reductio) - Reductio is a tool used to extract keywords and phrases using an implementation of the algorithm TextRank.
- [RegeributedTextView](https://github.com/rinov/RegeributedTextView) - RegeributedTextView is a subclass of UITextView that supports fully attribute string based on regular expression.
- [RSKGrowingTextView](https://github.com/ruslanskorb/RSKGrowingTextView) - A light-weight UITextView subclass that automatically grows and shrinks.
- [Splitflap](https://github.com/yannickl/Splitflap) - A simple split-flap display for your Swift applications. `UIKit`
- [styled-text](https://github.com/blueapron/styled-text) - Declarative text styles and streamlined Dynamic Type support for iOS.
- [StyledTextKit](https://github.com/GitHawkApp/StyledTextKit) - Declarative building and fast rendering attributed string library.
- [SwiftRichString](https://github.com/malcommac/SwiftRichString) - Elegant & Painless Attributed Strings Management Library in Swift.
- [SwiftyAttributes](https://github.com/eddiekaiger/SwiftyAttributes) - Swift extensions that make it a breeze to work with attributed strings. `iOS` `macOS` `tvOS` `watchOS`
- [SwiftyMarkdown](https://github.com/SimonFairbairn/SwiftyMarkdown) - Converts Markdown files and strings into NSAttributedString.
- [TCAnimatedText](https://github.com/jboullianne/TCAnimatedText) - TCAnimatedText is a SwiftUI package that adds animations to ordinary Text views. `SwiftUI`
- [TextAttributes](https://github.com/delba/TextAttributes) - An easier way to compose attributed strings.
- [TextfieldEffects](https://github.com/sumansid/TextfieldEffects) - A comprehensive extension file for all types of textfields styling written in swift for Xcode. `iOS`
- [TvOSTextViewer](https://github.com/dcordero/TvOSTextViewer) - Light and scrollable view controller for tvOS to present blocks of text. `tvOS`
- [TweetTextView](https://github.com/KarlZeo/TweetTextView) - This is a custom NSTextView to heighlight username hashtag and link. `macOS`
- [TwitterTextEditor](https://github.com/twitter/TwitterTextEditor) - A standalone, flexible API that provides a full featured rich text editor for iOS applications. `iOS` `UIKit`
- [Typographizer](https://github.com/frankrausch/Typographizer) - Fix dumb quotation marks and apostrophes in Swift. `Archived`
- [VisibleText](https://github.com/LeBzul/VisibleText) - Automatically determine the text color according to the background.
- [YanagiText](https://github.com/YuigaWada/YanagiText) - A lightweight TextView where can be attached any UIView.
- [YYText](https://github.com/ibireme/YYText) - Powerful text framework for iOS to display and edit rich text.

## Media and communication

### Asset pickers

- [AACameraView](https://github.com/EngrAhsanAli/AACameraView) - AACameraView is a lightweight, easy-to-use and customizable camera view framework written in Swift.
- [AGImageControls](https://github.com/agilie/AGImageControls) - cool tools for image edition.
- [ALCameraViewController](https://github.com/AlexLittlejohn/ALCameraViewController) - A camera view controller with custom image picker and image cropping. `iOS` `Archived`
- [AssetsPickerViewController](https://github.com/DragonCherry/AssetsPickerViewController) - Powerfully Customizable - Multiple Photo & Video Picker Controller.
- [ATGMediaBrowser](https://github.com/ounass-tech/ATGMediaBrowser) - Image slide-show viewer with multiple predefined transition styles, with ability to create new transitions with ease.
- [BarcodeScanner](https://github.com/hyperoslo/BarcodeScanner) - A simple and beautiful barcode scanner. `iOS`
- [Brightroom](https://github.com/FluidGroup/Brightroom) - An image editor and engine using CoreImage. `UIKit`
- [BRNImagePickerSheet](https://github.com/jacklevin74/BRNImagePickerSheet/tree/master) - A duplicate of that shiny new custom action sheet seen in iOS8's iMessage
- [BSImagePicker](https://github.com/mikaoj/BSImagePicker) - A multiple image picker for iOS.
- [BSZoomGridScrollView](https://github.com/boraseoksoon/BSZoomGridScrollView) - BSZoomGridScrollView is a powerful, pure swift iOS UI framework that provides the awesome grid scrollview containing your image array that are able to zoom, tracking your touch area. `SwiftUI` `UIKit`
- [CameraEngine](https://github.com/Winlentia/CameraEngine) - CameraEngine is an iOS camera engine library that allows easy integration of special capture features and camera customization in your iOS app.
- [CameraManager](https://github.com/imaginary-cloud/CameraManager) - Simple Swift class to provide all the configurations you need to create custom camera view in your app. `iOS`
- [Collage](https://github.com/sohamb1390/Collage) - A simple photo collage app with predefined collage frames.
- [ConvenientImagePicker](https://github.com/cloxnu/ConvenientImagePicker) - the new iOS image picker. Beautiful, delicate, and customizable. `iOS`
- [CSPhotoGallery](https://github.com/youkchansim/CSPhotoGallery) - This is very simple and light photo gallery.
- [DKImagePickerController](https://github.com/zhangao0086/DKImagePickerController) - Image Picker Controller for iOS.
- [DSFacebookImagePicker](https://github.com/daniel-sanche/DSFacebookImagePicker) - let your users add images from their Facebook albums
- [EFColorPicker](https://github.com/EFPrefix/EFColorPicker) - EFColorPicker is a lightweight color picker in Swift. `iOS` `Archived`
- [EmojiPickerUI](https://github.com/insidegui/EmojiPickerUI) - A framework implementing a macOS-style emoji picker for iPadOS.
- [FAImageCropper](https://github.com/fahidattique55/FAImageCropper) - Image Cropper like Instagram. `iOS`
- [FMPhotoPicker](https://github.com/congnd/FMPhotoPicker) - FMPhotoPicker is a modern, simple and zero-dependency photo picker with an elegant and customizable image editor. `iOS`
- [Fusuma](https://github.com/ytakzk/Fusuma) - Instagram-like photo browser and a camera feature with a few line of code in Swift. `iOS`
- [ImageCropper](https://github.com/nkopilovskii/ImageCropper) - Module for implementing the process of cropping images. `iOS`
- [ImagePicker](https://github.com/hyperoslo/ImagePicker) - Reinventing the way ImagePicker works. `iOS`
- [ImagePickerTrayController](https://github.com/lerboe/ImagePickerTrayController) - ImagePickerTrayController is a component that replicates the custom photo action sheet in iMessage.
- [ImageViewer.swift](https://github.com/michaelhenry/ImageViewer.swift) - An easy to use Image Viewer that is inspired by Facebook. `iOS`
- [INSPhotoGallery](https://github.com/m1entus/INSPhotoGallery) - INSPhotoGallery is a modern looking photo gallery written in Swift for iOS.
- [iOS-swift-MSCrop](https://github.com/chetanpanchal94/iOS-swift-MSCrop) - A view which can be moved and scaled, that allows user to select the cropping area in an image.
- [kanvas](https://github.com/tumblr/kanvas-ios) - Kanvas is an open-source iOS library for adding effects, drawings, text, stickers, and making GIFs from existing media or the camera.
- [LiquidLoader](https://github.com/yoavlt/LiquidLoader) - Spinner loader components with liquid animation.
- [Mantis](https://github.com/guoyingtao/Mantis) - A photo cropping tool which mimics Photo.app. `iOS` `SwiftUI` `UIKit`
- [NextLevel](https://github.com/NextLevel/NextLevel) - NextLevel is a Swift camera system designed for easy integration, customized media capture, and image streaming in iOS. Integration can optionally leverage AVFoundation or ARKit. `iOS`
- [NKVPhonePicker](https://github.com/NikKovIos/NKVPhonePicker) - An UITextField subclass to simplify country code's picking. `iOS`
- [photo-editor](https://github.com/mhm-ibrahim/photo-editor) - Photo editor with a lot of cool features.
- [PhotoCropEditor](https://github.com/sprint84/PhotoCropEditor) - Framework written in Swift for Cropping Images easily.
- [PixelSDK](https://github.com/GottaYotta/PixelSDK) - Pixel SDK is a photo and video editing framework written in Swift. `iOS`
- [PKCCrop](https://github.com/pikachu987/PKCCrop)
- [preview-transition](https://github.com/Ramotion/preview-transition) - PreviewTransition is a simple preview gallery controller. `iOS`
- [PrismaSimpleImagePicker](https://github.com/liangdrime/PrismaSimpleImagePicker) - This is a copy of the Prisma APP. Reproduce Prisma custom camera, image picker and picture editor.
- [QCropper](https://github.com/qchenqizhi/QCropper) - This project aims to provide an image cropping experience like iOS Photos.app. `iOS`
- [SKPhotoBrowser](https://github.com/suzuki-0000/SKPhotoBrowser) - Simple PhotoBrowser/Viewer inspired by facebook, twitter photo browsers written by swift.
- [SwiftMustaches](https://github.com/elpassion/SwiftMustaches) - iOS 8 Photo Editing Extension that adds mustaches to your face
- [SwiftVideoBackground](https://github.com/dingwilson/SwiftVideoBackground) - SwiftVideoBackground is an easy to use Swift framework that provides the ability to play a video on any UIView. `iOS`
- [SwiftyCam](https://github.com/Awalz/SwiftyCam) - A Snapchat Inspired iOS Camera Framework written in Swift.
- [TGLAugmentedRealityView](https://github.com/gleue/TGLAugmentedRealityView) - Augmented Reality made easy -- place overlays on a camera preview and adjust their position depending on device attitude. `Archived`
- [TLPhotoPicker](https://github.com/tilltue/TLPhotoPicker) - Multiple phassets picker for iOS lib. like a facebook.
- [TLStoryCamera](https://github.com/timelessg/TLStoryCamera)
- [Videoshader](https://github.com/snakajima/videoshader) - Script-based real-time video processing technology for OpenGL/iOS
- [YPImagePicker](https://github.com/Yummypets/YPImagePicker) - Instagram-like image picker & filters for iOS. `iOS`

### Audio

- [ATAudioWave](https://github.com/amrittrivedir/ATAudioWave) - create wave forms from audio.
- [Audio-Recorder](https://github.com/venkatkukunuru/Audio-Recorder) - Recording voice in swift.
- [AudioEqualizer](https://github.com/KiranPatelSpaceo/AudioEqualizer) - AudioEqualizer in swift.
- [AudioKit](https://github.com/AudioKit/AudioKit) - Open-source audio synthesis, processing, & analysis platform. `iOS` `macOS` `tvOS`
- [FDWaveformView](https://github.com/fulldecent/FDWaveformView) - FDWaveformView is an easy way to display an audio waveform in your app. It is a nice visualization to show a playing audio file or to select a position in a file. `iOS`
- [FRadioPlayer](https://github.com/fethica/FRadioPlayer) - A simple radio player framework for iOS, macOS, tvOS. `iOS`
- [InstaBars](https://github.com/vaibhavxyz/InstaBars) - InstaBars is a simple animation for iOS applications inspired by equaliser in instagram application.
- [Jukebox](https://github.com/teodorpatras/Jukebox) - Player for streaming local and remote audio files. Written in Swift. `Archived`
- [MLAudioPlayer](https://github.com/micheltlutz/MLAudioPlayer) - AudioPlayer for Swift projects. `Archived`
- [Muzonchik](https://github.com/yarodevuci/Muzonchik) - iOS Music App that let you search, download and play music `iOS`
- [Piano](https://github.com/saoudrizwan/Piano) - Easily play combinations of sound effects and Taptic Engine vibrations on iOS. `iOS`
- [SoundFonts](https://github.com/bradhowes/SoundFonts) - Simple iOS synthesizer that uses sound fonts for sound generation. `iOS`
- [SubtleVolume](https://github.com/andreamazz/SubtleVolume) - Replace the system volume popup with a more subtle indicator.
- [SwiftAudio](https://github.com/jorgenhenrichsen/SwiftAudio) - Audio player for iOS. `iOS`
- [SwiftySound](https://github.com/adamcichy/SwiftySound) - Swifty Sound is a simple library that lets you play sounds with a single line of code. `iOS` `macOS` `tvOS`
- [TuningFork](https://github.com/comyar/TuningFork) - TuningFork is a simple utility for processing microphone input and interpreting pitch, frequency, amplitude, etc. `Archived`

### Images

- [AImage](https://github.com/wangjwchn/AImage) - An animated gif & apng engine for iOS in Swift. Have a great performance on memory and cpu usage.
- [ARNZoomImageTransition](https://github.com/xxxAIRINxxx/ARNZoomImageTransition) - Custom image zooming animation transition & interactive transition. written in Swift.
- [BitmapCanvas](https://github.com/nst/BitmapCanvas) - Bitmap offscreen drawing in Swift for OS X. `macOS`
- [cocoa-close-pixelate](https://github.com/bmaslakov/cocoa-close-pixelate) - Cocoa port of https://github.com/desandro/close-pixelate `iOS`
- [cyborg](https://github.com/uber/cyborg) - Display Android Vectordrawables on iOS.
- [DPImageCache](https://github.com/dphans/DPImageCache) - Swift extension for UIImageView. Help loading image asynchronously and store local file cache.
- [DPImageGenerator](https://github.com/dwipp/DPImageGenerator) - It's an image generator for default image.
- [EFQRCode](https://github.com/EFPrefix/EFQRCode) - A better way to operate quick response code in Swift. `iOS` `watchOS`
- [FaceAware](https://github.com/BeauNouvelle/FaceAware) - An extension that gives UIImageView the ability to focus on faces within an image. `iOS` `Archived`
- [FlexibleImage](https://github.com/kawoou/FlexibleImage) - A simple way to play with image! `iOS` `macOS` `tvOS` `watchOS`
- [fog-machin](https://github.com/ngageoint/fog-machine) - The Fog Machine framework is a research and development effort to harness the computing power of multiple, locally connected iOS devices.
- [Gifu](https://github.com/kaishin/Gifu) - High-performance animated GIF support for iOS in Swift.
- [GPUImage2](https://github.com/BradLarson/GPUImage2) - GPUImage 2 is a BSD-licensed Swift framework for GPU-accelerated video and image processing.
- [Haneke](https://github.com/Haneke/HanekeSwift) - A lightweight generic cache for iOS written in Swift with extra love for images.
- [Image360](https://github.com/Ssimboss/Image360) - Special view & controller to display 360° panoramic images.
- [ImageButter](https://github.com/dollarshaveclub/ImageButter) - Makes dealing with images buttery smooth (WebP). `iOS`
- [ImageLoaderSwift](https://github.com/hirohisa/ImageLoaderSwift) - A lightweight and fast image loader for iOS written in Swift.
- [ImageViewer](https://github.com/Krisiacik/ImageViewer) - An image viewer à la Twitter.
- [JLStickerTextView](https://github.com/Textcat/JLStickerTextView) - Add text(multiple line support) to imageView, edit, rotate or resize them as you want, then render the text on image.
- [LetterAvatarKit](https://github.com/vpeschenkov/LetterAvatarKit) - UIImage extension that generates letter-based avatars written in Swift. `iOS` `tvOS` `UIKit`
- [LPThumbnailView](https://github.com/luispadron/LPThumbnailView) - A thumbnail view for iOS to give context to multiple images/videos using thumbnails and counter. `iOS` `UIKit` `Archived`
- [moa](https://github.com/evgenyneu/moa) - An image download extension of the image view written in Swift for iOS, tvOS and macOS.
- [Nuke](https://github.com/kean/Nuke) - Advanced pure Swift framework for loading, caching, processing, displaying and preheating images.
- [Panorama](https://github.com/amkraft/Panorama) - 360° panorama view, iOS-
- [Panoramic](https://github.com/iSame7/Panoramic) - Swift implementation of the photo tilt gesture/UX found in Facebook's Paper app.
- [Panorific](https://github.com/ndmeiri/Panorific) - An immersive, intuitive, motion-based way to explore high quality panoramas and photos on an iOS device. Panorific is implemented in Swift.
- [PASImageView](https://github.com/abiaad/PASImageView) - Rounded async imageview downloader lightly cached and written in Swift.
- [PuzzleMaker](https://github.com/PGSSoft/PuzzleMaker) - Swift framework responsible for generating puzzles from the image. `iOS`
- [ShadowImageView](https://github.com/olddonkey/ShadowImageView) - An apple music cover picture shadow style image library.
- [Sharaku](https://github.com/makomori/Sharaku) - Image filtering UI library like Instagram. `iOS`
- [Snowflake](https://github.com/onmyway133/Snowflake) - SVG in Swift. `iOS`
- [Sumo](https://github.com/1amageek/Sumo) - Sumo is a library that prepares for fast upload for iOS. It is effective when uploading by selecting images continuously. `iOS`
- [SwiftImageProcessing](https://github.com/skyfe79/SwiftImageProcessing) - Pixel operations in swift.
- [SwiftSVG](https://github.com/mchoe/SwiftSVG) - A single pass SVG parser with multiple interface options (String, NS/UIBezierPath, CAShapeLayer, and NS/UIView). `iOS` `macOS` `tvOS`
- [swiftui-image-viewer](https://github.com/Jake-Short/swiftui-image-viewer) - An image viewer built using SwiftUI. Featuring drag to dismiss, pinch to zoom, remote and local images, and more. `iOS` `SwiftUI`
- [SwiftUIImageEffects](https://github.com/globchastyy/SwiftUIImageEffects) - Swift port of Apple UIImage+UIImageEffecs category. `iOS` `UIKit`
- [SwiftyGif](https://github.com/alexiscreuzot/SwiftyGif) - High performance GIF engine.
- [Toucan](https://github.com/gavinbunney/Toucan) - Toucan is a Swift library that provides a clean, quick API for processing images.
- [Walt](https://github.com/gonzalonunez/Walt) - A Swift 3 library for creating gifs and videos from a series of images. `Archived`
- [WeScan](https://github.com/WeTransferArchive/WeScan) - Document Scanning Made Easy for iOS. `iOS` `Archived`
- [ZoomImageView](https://github.com/muukii/ZoomImageView) - UI component library to expand the photo, such as Apple's Photos app.

### Messaging

- [BubblePictures](https://github.com/glassipbel/BubblePictures) - Framework for iOS to show Bubble like pictures. `iOS`
- [chatheads](https://github.com/rajatgupta26/fk-ios-chatheads) - Library to use chat heads within your iOS app with complete physics and animations which drive multi user chat behaviour to support collapsed/stacked or expanded states.
- [ChatLayout](https://github.com/ekazaev/ChatLayout) - ChatLayout is an alternative solution to MessageKit. It uses custom UICollectionViewLayout to provide you full control over the presentation as well as all the tools available in UICollectionView.
- [Chatto](https://github.com/badoo/Chatto) - A lightweight framework to build chat applications, made in Swift.
- [ChatUI](https://github.com/iamshezad/ChatUI) - A simple chat app UI in SwiftUI. `SwiftUI`
- [CTFeedbackSwift](https://github.com/rizumita/CTFeedbackSwift) - Feedback mail composer for iOS re-written in Swift of CTFeedback.
- [FalconMessenger](https://github.com/RMizin/FalconMessenger) - 🌟🌟🌟🌟🌟 Falcon Messenger is a Fast and Beautiful cloud-based messaging app. With iOS and IPadOS Support. `iOS` `Archived`
- [FBChatClone](https://github.com/VamshiIITBHU14/FBChatClone) - This project is a clone of FB Messenger.
- [FirebaseChat](https://github.com/sohamb1390/FirebaseChat) - A simple anonymous group chat application using Firebase.
- [ForceBlur](https://github.com/Yalantis/ForceBlur) - ForceBlur Animation for iOS Messaging Apps. `iOS`
- [FTChatMessageDemoProject](https://github.com/liufengting/FTChatMessageDemoProject) - FTChatMessageDemoProject, a chat message ui framework written in swift. Not quite finished.
- [InAppNotify](https://github.com/lucabecchetti/InAppNotify) - Swift library to manage in app notification in swift language, like WhatsApp, Telegram, Frind, etc.
- [InitialsImageView](https://github.com/bachonk/InitialsImageView) - A simple UIImageView extension for using initials as a profile image, written in swift.
- [ListPlaceholder](https://github.com/malkouz/ListPlaceholder) - ListPlaceholder is a swift library allows you to easily add facebook style animated loading placeholder to your tableviews or collection views.
- [MessageBalloon](https://github.com/caiobzen/MessageBalloon) - A message balloon animation made with CoreAnimation.
- [MessageProgressView](https://github.com/Tueno/MessageProgressView) - Simple loading animation for Swift. `iOS`
- [MessageViewController](https://github.com/GitHawkApp/MessageViewController) - A SlackTextViewController replacement written in Swift for the iPhone X. `iOS` `UIKit`
- [Messenger](https://github.com/relatedcode/Messenger) - This is a native iOS Messenger app, making realtime chat conversations and audio calls with full offline support.
- [MessengerBubbles](https://github.com/RpX974/MessengerBubbles) - Create ImageView for User or Group like Messenger app.
- [MessengerKit](https://github.com/steve228uk/MessengerKit) - A UI framework for building messenger interfaces on iOS.
- [MMTextureChat](https://github.com/mukyasa/MMTextureChat) - AsyncDisplayKit(Texture) Smooth Scroll Chat Simulation. `iOS`
- [nio](https://github.com/niochat/nio) - Nio is an upcoming Matrix client for iOS. `iOS` `SwiftUI`
- [NMessenger](https://github.com/eBay/NMessenger) - A fast, lightweight messenger component built on AsyncDisplaykit and written in Swift. `Archived`
- [Postal](https://github.com/snipsco/Postal) - A swift framework for working with emails.
- [Quick-Chat](https://github.com/aslanyanhaik/Quick-Chat) - Real time chat app written in Swift 3 using Firebase. `iOS`
- [ReverseExtension](https://github.com/marty-suzuki/ReverseExtension) - UITableView extension that enabled to insert cell from bottom of tableView.
- [Rocket.Chat](https://github.com/RocketChat/Rocket.Chat.iOS) - Rocket.Chat Native iOS Application. `iOS` `Archived`
- [SupportEmail](https://github.com/schayes04/SupportEmail) - Prepopulates emails with support information in iOS apps. `Archived`
- [swift-chat](https://github.com/googlearchive/ios-swift-chat-example) - FireChat implemented in Swift!. `Archived`
- [SwiftyChat](https://github.com/EnesKaraosman/SwiftyChat) - Simple Chat Interface to quick start with built-in message cells. `iOS` `macOS` `SwiftUI`
- [Toolbar](https://github.com/1amageek/Toolbar) - Awesome autolayout Toolbar. `iOS`
- [Twitter_Post](https://github.com/gaborcsontos/Twitter_Post) - Custom Twitter Post View Controller.

### Speech recognition

- [SayWhat](https://github.com/marcdown/SayWhat) - Spotify artist search using speech recognition.

### Video

- [Cabbage](https://github.com/VideoFlint/Cabbage) - A video composition framework build on top of AVFoundation. It's simple to use and easy to extend.
- [CTPanoramaView](https://github.com/scihant/CTPanoramaView) - A library that displays spherical or cylindrical panoramas with touch or motion based controls.
- [Fisheye](https://github.com/hanton/Fisheye) - iOS 360° panorama video player with Metal rendering support (formerly HTY360Player) `iOS`
- [FloatingPlayer](https://github.com/engmahsa/FloatingPlayer) - A Swift floating player like YouTube player, using AVPlayer.
- [FrameGrabber](https://github.com/arthurhammer/FrameGrabber) - iOS app to extract full-resolution video frames as images. `iOS` `Archived`
- [MBVideoPlayer](https://github.com/mwaqasbhati/MBVideoPlayer) - A video player on top of AVQueuePlayer with custom header, playlist items, play, pause, seek to slider, time, resize to fullscreen, forward, backward horizontal, vertical capabilities. `iOS`
- [MMPlayerView](https://github.com/MillmanY/MMPlayerView) - Custom AVPlayerLayer on view and transition player with good effect like youtube and facebook.
- [mobileplayer-ios](https://github.com/sahin/mobileplayer-ios) - A powerful and completely customizable media player for iOS. `iOS`
- [Periscope-VideoViewController](https://github.com/gontovnik/Periscope-VideoViewController) - Video view controller with Periscope fast rewind control.
- [PryntTrimmerView](https://github.com/HHK1/PryntTrimmerView) - A set of tools to trim, crop and select frames inside a video. `iOS`
- [SGPlayer](https://github.com/libobjc/SGPlayer) - A powerful media player framework for iOS, macOS, and tvOS. Support 360° panorama video, VR video. RTMP streaming. `iOS` `macOS` `tvOS`
- [Swifty360Player](https://github.com/abdullahselek/Swifty360Player) - iOS 360-degree video player streaming from an AVPlayer.
- [TVVLCPlayer](https://github.com/kodlian/TVVLCPlayer) - TVVLCPlayer lets you integrate easily a powerfull video player with playback control views to your tvOS apps. `tvOS`
- [VersaPlayer](https://github.com/josejuanqm/VersaPlayer) - Versatile Video Player implementation for iOS, macOS, and tvOS. `iOS`
- [VideoTimelineView](https://github.com/Tomohiro-Yamashita/VideoTimelineView) - Video timeline UI for iOS Apps. `iOS`
- [VRDemo-Swift](https://github.com/Huanhoo/VRDemo-Swift) - RDemo-Swift is a 360-degree video player demo which achieved use Swift3.0 and OpenGL ES.

### Web views and previews

- [ReadabilityKit](https://github.com/exyte/ReadabilityKit) - Preview extractor for news, articles and full-texts in Swift. `Archived`
- [SCWebPreview](https://github.com/myoungsc/SCWebPreview) - Preview content in website.
- [SwiftLinkPreview](https://github.com/leonardocardoso/SwiftLinkPreview) - It makes a preview from an url, grabbing all the information such as title, relevant texts and images. `iOS` `macOS` `tvOS` `watchOS` `Archived`
- [TLMetaResolver](https://github.com/tryolabs/TLMetaResolver) - TLMetaResolver is an extension to UIWebView writen in Swift that adds the ability to parse the meta tags in the loaded web page and extract information about a native app that can be deep linked from that page.
- [URLEmbeddedView](https://github.com/marty-suzuki/URLEmbeddedView) - URLEmbeddedView automatically caches the object that is confirmed the Open Graph Protocol. `iOS` `tvOS`
- [URLPreview](https://github.com/itsmeichigo/URLPreview) - An NSURL extension for showing preview info of webpages.

## Data and infrastructure

### Architecture

- [CleanStore](https://github.com/Clean-Swift/CleanStore) - A sample iOS app built using the Clean Swift architecture.
- [PresenterKit](https://github.com/jessesquires/PresenterKit) - ⚠️ Deprecated ⚠️ `iOS` `Archived`
- [Swift-VIPER-Module](https://github.com/Juanpe/Swift-VIPER-Module) - Xcode template for VIPER Architecture written in Swift 3. `Archived`
- [Transporter](https://github.com/DenTelezhkin/Transporter) - Transporter is a modern finite-state machine implemented in pure Swift.

### Concurrency

- [Async](https://github.com/duemunk/Async) - Syntactic sugar in Swift for asynchronous dispatches in Grand Central Dispatch.
- [AsyncConcurrentQueue](https://github.com/mredig/AsyncConcurrentQueue) - A FIFO queuing system leveraging Swift's async/await structured concurrency. Also includes FutureTask which allows you to arbitrairily delay/start a task.
- [Chronos-Swift](https://github.com/comyar/Chronos-Swift) - GCD Utilities. `Archived`
- [ConcurrencyPlus](https://github.com/ChimeHQ/ConcurrencyPlus) - Utilities for working with Swift Concurrency. `iOS` `macOS` `Archived`
- [MainThreadPropertyAccessor](https://github.com/theisegeberg/MainThreadPropertyAccessor) - Syntactic sugar for setting properties on an ObservableObject on the main thread from within a Task.
- [Overdrive](https://github.com/saidsikira/Overdrive) - Fast async task based API in Swift with focus on type safety, concurrency and multi threading. `Archived`
- [Queuer](https://github.com/FabrizioBrancati/Queuer) - Queuer is a queue manager, built on top of OperationQueue and Dispatch (aka GCD). `macOS` `tvOS` `watchOS`
- [Retry](https://github.com/icanzilb/Retry) - Haven't you wished for `try` to sometimes try a little harder? Meet `retry`.
- [swift-async-queue](https://github.com/dfed/swift-async-queue) - A queue that enables sending FIFO-ordered tasks from synchronous to asynchronous contexts.
- [TaskMeeting](https://gist.github.com/NikolaiRuhe/c98005245d7b6e25328752cf0680675c) -  A type that synchronizes progress of two tasks.

### Dates and scheduling

- [10Clock](https://github.com/joedaniels29/10Clock) - This Control is a beautiful time-of-day picker heavily inspired by the iOS 10 "Bedtime" timer.
- [Countdown](https://github.com/leonardobilia/Countdown) - The Countdown timer app allows you to start, pause, reset and set up optional alarm sounds as you wish. `iOS` `SwiftUI`
- [MagicTimer](https://github.com/MagicTimerFW/MagicTimer) - MagicTimer is a UIView based timer that displays a countdown or count-up timer. `iOS`
- [RateLimit](https://github.com/soffes/RateLimit) - Simple utility for only executing code every so often. `iOS` `macOS` `tvOS` `watchOS` `Archived`
- [Runner](https://github.com/lucianomarisi/Runner) - Execute a block at specific time intervals.
- [Schedule](https://github.com/luoxiu/Schedule) -  Lightweight timed task scheduler for Swift.
- [SnapTimer](https://github.com/andresinaka/SnapTimer) - Implementation of Snapchat's stories timer.
- [SwiftClockUI](https://github.com/renaudjenny/SwiftClockUI) - Clock UI for SwiftUI. `iOS` `macOS` `SwiftUI`
- [SwiftDate](https://github.com/malcommac/SwiftDate) - Powerful NSDate & Time Zones Management.
- [Timepiece](https://github.com/naoty/Timepiece) - Intuitive date handling in Swift.
- [TimeZonePicker](https://github.com/gligorkot/TimeZonePicker) - A TimeZonePicker UIViewController similar to the iOS Settings app. Search and select from a range of cities and countries to find your most suitable time zone.

### Files and compression

- [AppFolder](https://github.com/dreymonde/AppFolder) - AppFolder is a lightweight framework that lets you design a friendly, strongly-typed representation of a directories inside your app folder. All the system directories like "Caches/" and "Application Support/" are already present, and you can add yours using just a few lines of code. `iOS`
- [Caramel](https://github.com/CaramelForSwift/Caramel) - A portable I/O framework for Swift. `Archived`
- [DAFileMonitor](https://github.com/dagostini/DAFileMonitor) - A simple wrapper around dispatch sources.
- [DirectoryObserver](https://github.com/dcvz/DirectoryObserver) - A microlibrary for monitoring directory changes
- [FileBrowser](https://github.com/marmelroy/FileBrowser) - Finder-style iOS file browser written in Swift.
- [FileExplorer](https://github.com/Augustyniak/FileExplorer) - FileExplorer is a powerful iOS file browser that allows its users to choose and remove files and/or directories.
- [FileKit](https://github.com/nvzqz/FileKit) - Simple and expressive file management in Swift.
- [Files](https://github.com/JohnSundell/Files) - A nicer way to handle files & folders in Swift.
- [GzipSwift](https://github.com/1024jp/GzipSwift) - Swift package that enables gzip/gunzip Data using zlib
- [KZFileWatchers](https://github.com/krzysztofzablocki/KZFileWatchers) - A micro-framework for observing file changes, both local and remote. Helpful in building developer tools.
- [SwiftFilePath](https://github.com/nori0620/SwiftFilePath) - Simple and powerful wrapper for NSFileManager.
- [UTIKit](https://github.com/cockscomb/UTIKit) - UTIKit is an UTI (Uniform Type Identifier) wrapper for Swift.
- [Warehouse](https://github.com/muukii/Warehouse) - You can use easily NSFileManager.
- [Zip](https://github.com/marmelroy/Zip) - Swift framework for zipping and unzipping files.

### JSON and serialization

- [Argo](https://github.com/thoughtbot/Argo) - Functional JSON parsing library for Swift.
- [mapper](https://github.com/lyft/mapper) - Another JSON deserialization library for Swift. `Archived`
- [Marshal](https://github.com/utahiosmac/Marshal) - Marshaling the typeless wild west of [String: Any]. `iOS`
- [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper) - Simple JSON Object mapping written in Swift
- [Serpent](https://github.com/ml-archive/Serpent) - A protocol to serialize Swift structs and classes for encoding and decoding. `Archived`
- [SwiftyJSON](https://github.com/SwiftyJSON/SwiftyJSON) - The better way to deal with JSON data in Swift.

### Networking

- [apollo-ios](https://github.com/apollographql/apollo-ios) - A strongly-typed, caching GraphQL client for iOS, written in Swift. `iOS`
- [Bridge](https://github.com/BridgeNetworking/Bridge) - Extensible HTTP Networking for iOS.
- [HTTPParser](https://github.com/ZewoGraveyard/HTTPParser) - HTTP parser for Swift 2 (Linux ready).
- [NetShears](https://github.com/divar-ir/NetShears) - NetShears is a Network interceptor framework written in Swift.
- [network](https://github.com/lovesunstar/network) - Making a chain-able request.
- [Reachability](https://github.com/ashleymills/Reachability.swift) - Replacement for Apple's Reachability re-written in Swift with closures.
- [sockets](https://github.com/vapor-community/sockets) - 🔌 Non-blocking TCP socket layer, with event-driven server and client.
- [SSASwiftReachability](https://github.com/SSA111/SSASwiftReachability) - A Swift Library To Track Network Reachability Changes.
- [WikipediaKit](https://github.com/Raureif/WikipediaKit) - API Client Framework for Swift 3 on macOS, iOS, watchOS, and tvOS. `iOS` `macOS` `tvOS` `watchOS` `Archived`

### Parsing and formatting

- [AnyFormatKit](https://github.com/luximetr/AnyFormatKit) - Text formatting framework written on Swift 5.0.
- [FeedKit](https://github.com/nmdias/FeedKit) - An RSS, Atom and JSON Feed parser written in Swift.
- [FolioReaderKit](https://github.com/FolioReader/FolioReaderKit) - A Swift ePub reader and parser framework for iOS. `iOS` `Archived`
- [Format](https://github.com/marmelroy/Format) - A Swift 2 formatter kit. Simple formatting syntax for decimal numbers, currency, addresses, ordinal numbers and hexadecimal colors.
- [Fuzi](https://github.com/cezheng/Fuzi) - A fast & lightweight XML & HTML parser in Swift that makes your life easier. `iOS`
- [Ji](https://github.com/honghaoz/Ji) - XML/HTML parser for Swift. `Archived`
- [Kanna](https://github.com/tid-kijyun/Kanna) - Kanna is an XML/HTML parser for macOS / iOS / tvOS.
- [phonenumberkit](https://github.com/marmelroy/PhoneNumberKit) - A Swift framework for parsing, formatting and validating international phone numbers. Inspired by Google's libphonenumber.
- [Regex](https://github.com/sharplet/Regex) - A Swift µframework providing an NSRegularExpression-backed Regex type.
- [SpotlightLyrics](https://github.com/jayasme/SpotlightLyrics) - An LRC file parser for iOS. `iOS`
- [StringFormatter](https://github.com/orucanil/StringFormatter) - Simple Text Formetter (Credit Card Number, Phone Number, Serial Number etc.) Can be used in all text inputs according to the format pattern. If desired, large minor character restrictions can be made in the format pattern. `iOS`
- [TPPDF](https://github.com/techprimate/TPPDF) - TPPDF is a simple-to-use PDF builder for iOS. `iOS`

### Persistence and caching

- [Aggregate](https://github.com/perlmunger/Aggregate) - How to build aggregate data fetch requests using Core Data.
- [AlecrimCoreData](https://github.com/alecrim/AlecrimCoreData) - AlecrimCoreData is a framework to easily access Core Data objects in Swift. `Archived`
- [Cache](https://github.com/hyperoslo/Cache) - Nothing but Cache. `iOS`
- [Cacher](https://github.com/raulriera/Cacher) - Super simple caching solution for iOS, macOS, tvOS and watchOS. `iOS` `macOS`
- [CoreStore](https://github.com/JohnEstropia/CoreStore) - Unleashing the real power of Core Data with the elegance and safety of Swift
- [Depot](https://github.com/iSame7/Depot) - Struct persistance framework for Swift.
- [GRDB](https://github.com/groue/GRDB.swift) - A versatile SQLite toolkit for Swift, with WAL mode support.
- [JSQDataSourcesKit](https://github.com/jessesquires/JSQDataSourcesKit) - ⚠️ Deprecated ⚠️ `iOS` `Archived`
- [Kuery](https://github.com/kishikawakatsumi/Kuery) - A type-safe Core Data query API using Swift 4's Smart KeyPaths.
- [Palau](https://github.com/symentis/Palau) - NSUserDefaults with Wings!.
- [Pantry](https://github.com/nickoneill/Pantry) - The missing light persistence layer for Swift. `Archived`
- [pencil](https://github.com/naru-jpn/pencil) - Super lightweight DB written in Swift.
- [QueryKit](https://github.com/QueryKit/QueryKit) - A simple CoreData query language for Swift and Objective-C.
- [redis](https://github.com/vapor/redis) - Vapor provider for RediStack
- [Seam](https://github.com/nofelmahmood/Seam) - Seamless CloudKit Sync with CoreData.
- [Shallows](https://github.com/dreymonde/Shallows) - Your lightweight caching toolbox.
- [SQLite.swift](https://github.com/stephencelis/SQLite.swift) - A type-safe, Swift-language layer over SQLite3.
- [TypedDefaults](https://github.com/tasanobu-zz/TypedDefaults) - TypedDefaults is a utility library to type-safely use NSUserDefaults.
- [WACoreDataSpotlight](https://github.com/Wasappli/WACoreDataSpotlight) - Automatically index your CoreData objects to CoreSpotlight on iOS 9.
- [yr-cachyr](https://github.com/nrkno/yr-cachyr) - A small key-value data cache for iOS, macOS and tvOS, written in Swift. `Archived`

### Server-side Swift

- [Aeon](https://github.com/ZewoGraveyard/Aeon) - Aeon is a GCD based HTTP server for Swift 2.
- [blackfire](https://github.com/elliottminns/blackfire) - A minimal, fast and unopinionated web framework for Swift `Archived`
- [CocoaHTTPServer](https://github.com/robbiehanson/CocoaHTTPServer) - A small, lightweight, embeddable HTTP server for Mac OS X or iOS applications.
- [Curassow](https://github.com/kylef-archive/Curassow) - Swift HTTP server using the pre-fork worker model. [And check out the rest at github/kylef!]
- [Dynamo](https://github.com/johnno1962/Dynamo) - High Performance (nearly)100% Swift Web server supporting dynamic content.
- [Express](https://github.com/crossroadlabs/Express) - Swift Express is a simple, yet unopinionated web application server written in Swift
- [Frank](https://github.com/kylef-archive/Frank) - Frank is a DSL for quickly writing web applications in Swift
- [Kitura](https://github.com/Kitura/Kitura) - Web framework and HTTP server for Swift by IBM
- [Perfect](https://github.com/PerfectlySoft/Perfect) - Server-side Swift. The Perfect library, application server, connectors and example apps.
- [swift-http](https://github.com/huytd/swift-http) - HTTP Implementation for Swift on Linux and Mac OS X
- [Swifter](https://github.com/httpswift/swifter) - Tiny http server engine written in Swift programming language.
- [Swifton](https://github.com/sauliusgrigaitis/Swifton) - A Ruby on Rails inspired Web Framework for Swift that runs on Linux and OS X
- [swiftra](https://github.com/takebayashi/swiftra) - Sinatra-like DSL for developing web apps in Swift
- [Taylor](https://github.com/izqui/Taylor) - A lightweight library for writing HTTP web servers with Swift
- [Trevi](https://github.com/Yoseob/Trevi) - A powerful Swift Web Application Server Framework Project
- [Vapor](https://github.com/vapor/vapor) - Elegant web framework for Swift that works on iOS, OS X, and Ubuntu.
- [Zewo](https://github.com/Zewo/Zewo) - Venice based HTTP server for Swift 2.2 on Linux

## System integration

### Bluetooth and beacons

- [BeaconMonitor](https://github.com/sebk/BeaconMonitor) - Swift framework to monitor and range iBeacons
- [Bleu](https://github.com/1amageek/Bleu) - BLE (Bluetooth LE) for U. `iOS`
- [bluejay](https://github.com/steamclock/bluejay) - A simple Swift framework for building reliable Bluetooth LE apps. `iOS`
- [BluetoothKit](https://github.com/rhummelmose/BluetoothKit) - Easily communicate between iOS/OSX devices using BLE.
- [HiBeacons](https://github.com/nicktoumpelis/HiBeacons) - An iBeacons example app for iOS 10, with Apple Watch (watchOS 3.0) support, written in Swift 3. `iOS`
- [SwiftLocation](https://github.com/malcommac/SwiftLocation) - Sexy Location Manager and Beacon Monitoring for Swift.

### Device information

- [AssistantKit](https://github.com/anatoliyv/AssistantKit) - Easy way to detect device environment. `iOS`
- [CheckDevice](https://github.com/ugurethemaydin/CheckDevice) - CheckDevice is detected the current  device model and screen sizes.
- [Device](https://github.com/Ekhoo/Device) - Light weight tool for detecting the current device and screen size written in swift. `iOS` `macOS`
- [Luminous](https://github.com/andrealufino/Luminous) - Luminous gives you all the system information you need (Network, Locale, Carrier...) `iOS`
- [UIDeviceComplete](https://github.com/Nirma/UIDeviceComplete) - UIDevice extensions that fill in the missing pieces. `iOS`

### Localization

- [iOS-CustomLocalisator](https://github.com/micazeve/iOS-CustomLocalisator) - A custom localisator class which allows to change the app language without having to restart it.
- [Laurine](https://github.com/JiriTrecak/Laurine) - Localization code generator written in Swift.
- [Localize-Swift](https://github.com/marmelroy/Localize-Swift) - Swift 2.0 friendly localization and i18n with in-app language switching.

### Maps and location

- [AnimatePolyline](https://github.com/goldmoment/AnimatePolyline) - The animate polyline like Uber for GoogleMaps
- [ARCarMovement](https://github.com/antonyraphel/ARCarMovement) - This is navigation example on google map. Here Marker move as vehicles moves with turns as uber does in their app. Using old and new coordinates animating bearing value the markers are moving.
- [ASMapLauncher](https://github.com/abdullahselek/ASMapLauncher) - ASMapLauncher is a library for iOS written in Swift that helps navigation with various mapping applications.
- [curvyRoute](https://github.com/seatcode/curvyRoute) - Drawing curvy routes with MapKit. `iOS` `Archived`
- [DistancePicker](https://github.com/qmathe/DistancePicker) - Custom UIKit control to select a distance with a pan gesture, written in Swift. `iOS` `UIKit`
- [DynamicBubble](https://github.com/0xNSHuman/DynamicBubble) - Interactive Speech Balloon/Bubble view with rich customization UI for app user.
- [FlyoverKit](https://github.com/SvenTiigi/FlyoverKit) - 360° flyover on an MKMapView.
- [GeoTrackKit](https://github.com/intere/GeoTrackKit) - A Cocoapod for Geo Tracking. `iOS`
- [GooglePlacesClone](https://github.com/VishalNandoriya/GooglePlacesClone) - This repository aims for a tutorial on how to use the Google Places API in conjunction with Google Maps iOS SDK.
- [GpxLocationManager](https://github.com/vermont42/GpxLocationManager) - GpxLocationManager is a replacement for CLLocationManager that allows the developer to use GPS data from GPX files or CLLocation arrays for testing.
- [HHMarker](https://github.com/HilalAH/HHMarker) - using a .dae model as a marker in google maps
- [JDSwiftHeatMap](https://github.com/jamesdouble/JDSwiftHeatMap) - JDSwiftMap is an IOS Native MapKit Library. You can easily make a highly customized HeatMap.
- [MBMapPulseAnimation](https://github.com/ManickB/MBMapPulseAnimation)
- [NearBy](https://github.com/VishalNandoriya/NearBy) - iOS app to find nearby places using MapKit.
- [PRGLocationSearchBar](https://github.com/ispiropoulos/PRGLocationSearchBar) - Control used to show a search bar which can fetch your location as well as geocode a search string.
- [ScrollViewMinimap](https://github.com/nicoelayda/ScrollViewMinimap) - ScrollViewMinimap is a control for adding minimap functionality to UIScrollView. `iOS` `SwiftUI`
- [SnapLocation](https://github.com/ziligy/SnapLocation) - Swift micro-app that snaps your current location and writes it to pasteboard, it also optionally saves a map image in photos.
- [STLocationRequest](https://github.com/SvenTiigi/STLocationRequest) - UIViewController-Extension which is used to request the User-Location, at the very first time, in a simple and elegent way written in Swift. `Archived`
- [SwiftLoggly](https://github.com/vigneshuvi/SwiftLoggly) - Simple way to logging with rich feature framework in Swift.

### Payments

- [caishen](https://github.com/prolificinteractive/Caishen) - A Payment Card UI & Validator for iOS.
- [card.io](https://github.com/card-io/card.io-iOS-SDK) - card.io provides fast, easy credit card scanning in mobile apps. `Archived`
- [CreditCardForm](https://github.com/orazz/CreditCardForm-iOS) - CreditCardForm-iOS is an iOS demo app that allows developers to create the UI which replicates an actual Credit Card.
- [Money](https://github.com/danthorpe/Money) - Swift value types for working with money & currency. `Archived`
- [SwiftyStoreKit](https://github.com/bizz84/SwiftyStoreKit) - Lightweight In App Purchases Swift framework for iOS 8.0+ and OSX 9.0+. `iOS` `macOS` `tvOS`
- [ThinCreditCard](https://github.com/tsarikovskiy/ThinCreditCard) - Simple way to add a credit card.
- [TinyCreditCard](https://github.com/bestwnh/TinyCreditCard) - A clear and animated credit card input workflow implement. `iOS`

### Permissions

- [Arek](https://github.com/ennioma/arek) - AREK is a clean and easy to use wrapper over any kind of iOS permission. `Archived`
- [PAPermissions](https://github.com/pascalbros/PAPermissions) - A unified API to ask for permissions on iOS.
- [Permission](https://github.com/delba/Permission) - A unified API to ask for permissions on iOS.
- [PermissionScope](https://github.com/nickoneill/PermissionScope) - Intelligent iOS permissions UI and unified API. `Archived`
- [PermissionsKit](https://github.com/sparrowcode/PermissionsKit) - Universal API for request permission and get its statuses. `iOS`
- [PermissionsSwiftUI](https://github.com/jevonmao/PermissionsSwiftUI) - A SwiftUI package to handle permissions. `iOS` `macOS` `SwiftUI`
- [PermissionWizard](https://github.com/debug45/PermissionWizard) - It is an ultimate tool for system permissions management. `iOS` `macOS`
- [Proposer](https://github.com/nixzhu/Proposer) - Proposer provides a simple API to request permission for access Camera, Photos, Microphone, Contacts, Location.

### Security

- [EnigmaKit](https://github.com/mikaoj/EnigmaKit) - Enigma encryption in Swift.
- [Simplicity](https://github.com/SimplicityMobile/Simplicity) - A simple way to implement Facebook and Google login in your iOS and OS X apps. `iOS`
- [SwCrypt](https://github.com/soyersoyer/SwCrypt) - RSA public/private key generation, RSA, AES encryption/decryption, SEM encryption in Swift with CommonCrypto in iOS and OS X. `iOS` `macOS`
- [Swift.nV](https://github.com/NetSPI/Swift.nV) - Security Training Tool that demonstrates common mobile application vulnerabilities using Swift in iOS. `Archived`

## Games and machine learning

### Augmented reality

- [3DSnakeAR](https://github.com/PGSSoft/3DSnakeAR) - Well known game Snake written in Swift using ARKit. `iOS`
- [ARCharts](https://github.com/Boris-Em/ARCharts) - Lovely Augmented Reality Charts for iOS - Built with ARKit. `iOS`
- [ARDominoes](https://github.com/kkorouei/ARDominoes) - Create paths for your Augmented Reality environments using just points to represent the centre of the path.
- [ARKit-CoreLocation](https://github.com/AndrewHartAR/ARKit-CoreLocation) - Combines the high accuracy of AR with the scale of GPS data.
- [ARKit-Sampler](https://github.com/shu223/ARKit-Sampler) - Code examples for ARKit. `iOS`
- [ARKit-SCNPath](https://github.com/maxxfrazer/ARKit-SCNPath) - Create paths for your Augmented Reality environments using just points to represent the centre of the path. `iOS`
- [ARPaint](https://github.com/oabdelkarim/ARPaint) - Draw with bare fingers in the air using ARKit. `iOS`
- [ARSolar](https://github.com/emadhegab/ARSolar) - Solar System with ARKit on Swift.
- [ARSolarPlaySwift](https://github.com/miliPolo/ARSolarPlaySwift) - Solar System on Swift & ARKit. `iOS`
- [ARuler](https://github.com/duzexu/ARuler) - Mesure distance using apple ARKit.
- [ARViewer](https://github.com/farice/ARShooter/tree/master/ARViewer) - A demo Augmented Reality shooter made with ARKit in Swift (iOS 11) `iOS`
- [augmented-card](https://github.com/vigetlabs/augmented-card) - Example project for ARKit Image Tracking blog post `iOS`
- [Awesome-ARKit](https://github.com/olucurious/Awesome-ARKit) - A curated list of awesome ARKit projects and resources. `iOS`
- [baraba](https://github.com/nsoojin/baraba) - Make your UIScrollView scroll automatically when user is looking 👀 by tracking face using ARKit and AVFoundation. `iOS`
- [Findme](https://github.com/mmoaay/Findme) - An ARKit App that can help your friends to find you. `iOS`
- [Morse-Vision](https://github.com/acotilla91/Morse-Vision) - More Vision is a simple app that utilizes ARKit to interpret blinks as morse code which are then transcribed to text.
- [RealityKit-CardFli](https://github.com/maxxfrazer/RealityKit-CardFlip) - An example app using Apple's new RealityKit framework. `iOS`

### GameplayKit

- [GameplayKit: beyond games](https://github.com/zats/Presentations/tree/master/GameplayKit) - Various talks and corresponding sample code

### Machine learning

- [AIToolbox](https://github.com/KevinCoble/AIToolbox) - A toolbox of AI modules written in Swift: Graphs/Trees, Linear Regression, Support Vector Machines, Neural Networks, PCA, KMeans, Genetic Algorithms, MDP, Mixture of Gaussians.
- [awesome-machine-learning](https://github.com/onmyway133/awesome-machine-learning) - 🎰 A curated list of machine learning resources, preferably CoreML
- [Bender](https://github.com/xmartlabs/Bender) - Easily craft fast Neural Networks on iOS! Use TensorFlow models. Metal under the hood. `iOS`
- [Blog-Getting-Started-with-Vision](https://github.com/jeffreybergier/Blog-Getting-Started-with-Vision) - Blog: Getting Started with Vision on iOS 11.
- [CoreML-samples](https://github.com/ytakzk/CoreML-samples) - Sample code for Core ML using ResNet50 provided by Apple and a custom model generated by coremltools. `iOS`
- [coreml-training](https://github.com/hollance/coreml-training) - Source code for my blog post series "On-device training with Core ML". `iOS`
- [EmojiIntelligence](https://github.com/BilalReffas/EmojiIntelligence) - Neural Network built in Apple Playground using Swift. `macOS`
- [FaceCropper](https://github.com/KimDarren/FaceCropper) - Crop faces, inside of your image, with iOS 11 Vision api. `iOS` `Archived`
- [HelloVision](https://github.com/SwiftBrain/HelloVision) - Vision framework example for my article. https://medium.com/compileswift/swift-world-whats-new-in-ios-11-vision-456ba4156bad
- [Lumina](https://github.com/dokun1/Lumina) - A camera designed in Swift that can use any CoreML model for object recognition, as well as streaming video, images, and qr/bar codes. `iOS`
- [MLCameraDemo](https://github.com/stringcode86/MLCameraDemo) - Demonstrates using Vision with Core ML to preprocess AVCaptureVideoDataOutput and perform image classification.
- [pose](https://github.com/rdv0011/pose) - Estimates a human pose on an image.
- [Swift-AI](https://github.com/Swift-AI/Swift-AI) - The Swift machine learning library. `iOS` `macOS`
- [SwiftOCR](https://github.com/NMAC427/SwiftOCR) - Fast and simple OCR library written in Swift. `iOS` `macOS`
- [TvOSScribble](https://github.com/dcordero/TvOSScribble) - Handwriting numbers recognizer for Siri Remote.
- [UnsplashExplorer-CoreML](https://github.com/ahmetws/UnsplashExplorer-CoreML) - Core ML demo app with Unsplash API. `iOS`
- [WhatDog](https://github.com/isflump/WhatDog) - An simple iOS Dog type recognition app built with CoreML and MobileNet Model.

### Metal

- [MaLiang](https://github.com/Harley-xk/MaLiang) - MaLiang is a painting framework based on Metal. `iOS`
- [Metal City](https://github.com/AndyQ/MetalCity) - MetalCity is night city scape full procedurally generated, for both iOS and macOS. `iOS` `macOS`
- [Metal2DScrollable](https://github.com/codelynx/Metal2DScrollable) - Demonstrate how to zoom and scroll MTKView using UIScrollView
- [Metalbrot](https://github.com/jtbandes/metalbrot-playground) - An interactive playground showing how to use Metal compute kernels.
- [MetalFilters](https://github.com/alexiscn/MetalFilters) - Instagram filters implemented in Metal. `iOS`
- [MetalPinch](https://github.com/AlchemicalBytes/MetalPinch) - A demo on how to use UIGestureRecognizers to pan and zoom in Metal.
- [MetalScope](https://github.com/ejeinc/MetalScope) - Metal-backed 360° panorama view for iOS. `iOS` `Archived`
- [sample-metal](https://github.com/dehesa/sample-metal) - Examples for Apple's Metal APIs (rendering and compute).
- [ShaderMania](https://github.com/markusmoenig/ShaderMania) - Create, edit, share and learn about Metal shaders on macOS and iOS. `iOS` `macOS`

### SceneKit

- [BioViewer](https://github.com/Androp0v/BioViewer) - Protein (.pdb, .cif and .fasta) viewer for iPhone, iPad and Mac, using SwiftUI + SceneKit. `macOS` `SwiftUI`

### SpriteKit

- [AJParticlesLoadingView](https://github.com/arpitjain03/AJParticlesLoadingView) - A completely customizable loading particles animation on a view using SpriteKit.
- [AngryBirdClone](https://github.com/hamitseyrek/AngryBirdClone) - usage SpriteKit for create an AngryBird Game Clone
- [Magnetic](https://github.com/efremidze/Magnetic) - Magnetic is a customizable bubble picker like the Apple Music genre selection. `iOS`
- [Orbit7](https://github.com/Aaron-A-zz/Orbit7) - Open Source iOS Game created in SpriteKit with Swift.
- [SKTiled](https://github.com/mfessenden/SKTiled) - Swift framework for working with Tiled assets in SpriteKit. `iOS`
- [SKTiledMap](https://github.com/wbcyclist/SKTiledMap) - A TMX TileMap framework for SpriteKit.
- [SpriteKitWithUIKitSample](https://github.com/ymmtshny/SpriteKitWithUIKitSample) `UIKit`

## Platform extensions

### Dock

- [DockProgress](https://github.com/sindresorhus/DockProgress) - Show progress in your app's Dock icon. `macOS`
- [NikeClockIcon](https://github.com/mtynior/NikeClockIcon) - A clock inspired by Nike Watch Face that can be displayed in macOS Dock. `macOS` `SwiftUI`

### Menu bar

- [AutomaticStatusBarColor](https://github.com/dk53/AutomaticStatusBarColor) - A zero line component to manage status bar color automaticly throughout your application.

### Screensavers

- [Brooklyn](https://github.com/pedrommcarrasco/Brooklyn) - Screensaver inspired by Apple's Event on October 30, 2018. `macOS`

### Watch faces

- [SpriteKitWatchFacePlaygroundBook](https://github.com/steventroughtonsmith/SpriteKitWatchFacePlaygroundBook) - Swift Playgrounds port of SpriteKitWatchFace. `watchOS`
- [TimeBoard](https://github.com/guisua/TimeBoard) - A verbose Apple Watch App / Watchface `watchOS`

### Widgets

- [swiftui-widgets-fitness](https://github.com/marioeguiluz/swiftui-widgets-fitness) - Example project with SwiftUI, Combine and Widgets, using Apple Fitness app UI as the base `SwiftUI`

### Windows

- [LaunchAtLogin-Legacy](https://github.com/sindresorhus/LaunchAtLogin-Legacy) - Add “Launch at Login” functionality to your macOS app in seconds `macOS` `Archived`
- [Settings](https://github.com/sindresorhus/Settings) - ⚙ Add a settings window to your macOS app in minutes `macOS` `SwiftUI`
- [Welcome2ProjectKit](https://github.com/HsiangHo/Welcome2ProjectKit) - Create a Xcode-like welcome window. `macOS`

## Developer tools

### Asset and code generation

- [convertappicon](https://github.com/kreait/convertappicon) - Converts a pdf into multiple app icons for iOS and watchOS. `macOS` `Archived`
- [LicensePlist](https://github.com/mono0926/LicensePlist) - iOS license plists generator. Carthage, CocoaPods and the libraries specified by YAML file are supported. `iOS`
- [Misen](https://github.com/tasanobu-zz/Misen) - Script to support easily using Xcode Asset Catalog in Swift.
- [Natalie](https://github.com/krzyzanowskim/Natalie) - Storyboard Code Generator. `Archived`
- [R](https://github.com/mac-cain13/R.swift) - Get strong typed, autocompleted resources like images, fonts and segues in Swift projects. `iOS` `tvOS` `watchOS`
- [ResourceInstantiatable](https://github.com/rizumita/ResourceInstantiatable) - iOS resources management framework in Swift2.
- [StampIcon](https://github.com/jorystiefel/stampicon) - Mac command line tool to imprint a text banner over a PNG icon, written in Swift.
- [SwiftGen](https://github.com/SwiftGen/SwiftGen) - A collection of Swift tools to generate Swift code (enums for your assets, storyboards, Localizable.strings, …). `iOS`

### Logging and debugging

- [Bagel](https://github.com/yagiz/Bagel) - a little native network debugging tool for iOS. `iOS` `macOS`
- [Bulk](https://github.com/FluidGroup/Bulk) - Bulk is pipeline based powerful & flexible logging framework.
- [CleanroomLogger](https://github.com/emaloney/CleanroomLogger) - A default CustomStringConvertible implementation for Swift type.
- [DefaultStringConvertible](https://github.com/jessesquires/DefaultStringConvertible) - \[DEPRECATED\] A default CustomStringConvertible implementation for Swift types `Archived`
- [Duration](https://github.com/SwiftStudies/Duration) - A simple Swift package for measuring and reporting the time taken for operations.
- [Evergreen](https://github.com/nilsvu/Evergreen) - Most natural Swift logging. `Archived`
- [JustLog](https://github.com/justeat/JustLog) - JustLog brings logging on iOS to the next level. It supports console, file and remote Logstash logging via TCP socket with no effort. Support for logz.io available. `iOS` `Archived`
- [Knuff](https://github.com/KnuffApp/Knuff) - The debug application for Apple Push Notification Service (APNs). `macOS`
- [Landmarks-with-Logging](https://github.com/greimers/Landmarks-with-Logging) - Sample project to demonstrate OSLog
- [Lighty](https://github.com/abdullahselek/Lighty) - Easy to use and lightweight logger in Swift.
- [LocalConsole](https://github.com/duraidabdul/LocalConsole) - This Swift Package makes on-device debugging easy with a convenient PiP-style console that can display items in the same way print() will in Xcode. `SwiftUI` `UIKit`
- [logkit](https://github.com/logkit/logkit) - An efficient logging library for OS X, iOS, watchOS, and tvOS – written in Swift. Log to console, file, HTTP service, or your own endpoint. Simple to get started, but smartly customizable.
- [MacSymbolicator](https://github.com/inket/MacSymbolicator) - A simple Mac app for symbolicating macOS/iOS crash reports. `iOS` `macOS`
- [printer](https://github.com/hemangshah/printer) - Want to print logs in a fancy way? Here's the Swift 3.x supported logger for you. `Archived`
- [Pulse](https://github.com/kean/Pulse) - Pulse is a powerful logging system. `iOS` `macOS` `SwiftUI`
- [RapidLogger](https://github.com/krishna706/RapidLogger) - Rapid Logger captures all the log and able to display in device with neat UI.
- [SwiftLogger](https://github.com/MKSG-MugunthKumar/SwiftLogger) - A Logging framework for Swift
- [SwiftTrace](https://github.com/johnno1962/SwiftTrace) - Trace Swift and Objective-C method invocations.
- [SwiftyBeaver](https://github.com/SwiftyBeaver/SwiftyBeaver) - Colorful, lightweight & fast logging in Swift 2. `iOS` `macOS`
- [TinyConsole](https://github.com/Cosmo/TinyConsole) - A tiny log console to display information while using your iOS app. Written in Swift 3. `iOS`
- [Watchdog](https://github.com/wojteklu/Watchdog) - Class for logging excessive blocking on the main thread. `iOS` `macOS`
- [Willow](https://github.com/Nike-Inc/Willow) - Willow is a powerful, yet lightweight logging library written in Swift.
- [XCGLogger](https://github.com/DaveWoodCom/XCGLogger) - A debug log framework for use in Swift projects. Allows you to log details to the console (and optionally a file), just like you would have with NSLog or println, but with additional information, such as the date, function name, filename and line number. `iOS` `macOS` `tvOS` `watchOS`

### Scripting and command-line tools

- [AppIcon](https://github.com/Nonchalant/AppIcon) - AppIcon generates *.appiconset contains each resolution image for iOS. `iOS`
- [ColorizeSwift](https://github.com/mtynior/ColorizeSwift) - Terminal string styling for Swift.
- [Diamond](https://github.com/johnno1962/Diamond) - Swift scripting made easy.
- [Marathon](https://github.com/JohnSundell/Marathon) - Marathon makes it easy to write, run and manage your Swift scripts. `Archived`
- [Shell](https://github.com/helje5/Shell) - Module exposing Unix command line tools as Swift 5 @dynamicCallable functions.
- [Swift-For-Scripting](https://github.com/artemnovichkov/Swift-For-Scripting) - A hand-curated collection of useful and informative Swift Scripting materials.
- [SwiftFormat](https://github.com/nicklockwood/SwiftFormat) - A command-line tool for formatting Swift code.
- [SwiftShell-Swift2.0](https://github.com/kareman/SwiftShell) - A Swift framework for shell scripting.

### Testing

- [FBSnapshotsViewer](https://github.com/Antondomashnev/FBSnapshotsViewer) - A mac os application that shows the failing snapshot tests from FBSnapshotTestCase. `macOS`
- [pxctest](https://github.com/plu/pxctest) - Execute tests in parallel on multiple iOS Simulators. `iOS` `Archived`

### Xcode extensions

- [Comment-Spell-Checker](https://github.com/velyan/Comment-Spell-Checker) - Xcode extension for spell checking and auto-correcting code comments.
- [Import](https://github.com/markohlebar/Import) - Xcode extension for adding imports from anywhere in the code. `macOS`
- [SwiftInitializerGenerator](https://github.com/Bouke/SwiftInitializerGenerator) - Xcode 8 Source Code Extension to Generate Swift Initializers.
- [SwiftLintXcodePlugin](https://github.com/p-x9/SwiftLintXcodePlugin) - SwiftLint Plugin for Xcode. `iOS`

## Learning and utilities

### Playgrounds and snippets

- [swift-algorithm-club](https://github.com/kodecocodes/swift-algorithm-club) - Algorithms and data structures in Swift, with explanations!.
- [swift-summary](https://github.com/jakarmy/swift-summary) - A summary of Apple's Swift language written on Playgrounds.
- [SwiftSnippets](https://github.com/onmyway133/SwiftSnippets) - A collection of Swift snippets to be used in Xcode. `iOS` `macOS`

### Resource lists

- [A collaborative list of awesome swift resources](https://github.com/matteocrippa/awesome-swift) - A collaborative list of awesome Swift libraries and resources. Feel free to contribute! `iOS`
- [A curated list of awesome iOS ecosystem, including Objective-C and Swift Projects.](https://github.com/vsouza/awesome-ios) - A curated list of awesome iOS ecosystem, including Objective-C and Swift Projects `iOS`
- [A curated list of awesome Swift frameworks](https://github.com/Wolg/awesome-swift) - A curated list of awesome Swift frameworks, libraries and software.
- [Awesome macOS](https://github.com/iCHAIT/awesome-macOS) -  A curated list of awesome applications, softwares, tools and shiny things for macOS. `macOS`
- [Awesome Open Source Mac Apps](https://github.com/jeffreyjackson/mac-apps) - Open Source Mac Apps
- [Awesome Server Side Swift](https://github.com/Awesome-Server-Side-Swift/TheList) - A list of Awesome Server Side Swift 3 projects
- [Awesome Swift Education](https://github.com/hsavit1/Awesome-Swift-Education) - All of the resources for Learning About Swift.
- [Cocoanetics Swift-Examples](https://github.com/Cocoanetics/Swift-Examples) - Cocoanetics Swift Examples
- [iOS architecture](https://github.com/onmyway133/awesome-ios-architecture) - :japanese_castle: Better ways to structure iOS apps `iOS`
- [List of awesome snippets, plugins, and extras for Xcode](https://github.com/jeffreyjackson/awesome-xcode) - List of awesome snippets, plugins, and extras for Xcode.
- [Open-source iOS apps](https://github.com/dkhamsing/open-source-ios-apps) - A collaborative list of open-source iOS, watchOS and tvOS apps. `iOS` `tvOS` `watchOS` `SwiftUI`
- [Open-Source macOS Apps](https://github.com/serhii-londar/open-source-mac-os-apps) - Awesome list of open source applications for macOS. `macOS`
- [SwiftKitz](https://github.com/SwiftKitz) - Collection of quality Swift kits (Appz, Storez, Datez, Notificationz, UIKitz, Graphicz).
- [The best FRP in iOS links.](https://gist.github.com/JaviLorbada/4a7bd6129275ebefd5a6)
- [Top App Developers](https://github.com/app-developers/top) - Top App Developers - September 2022
- [WWDC Students](https://github.com/wwdc) - This repository features the lists of WWDC scholarship entrants from each year, beginning in 2014.

### Swift extensions and utilities

- [APTargets](https://github.com/collinhundley/APTargets) - Adding UIControl targets, the right way.
- [Butterfly](https://github.com/wongzigii/Butterfly) - A lightweight library for integrating feedback module. `Archived`
- [Cast Free Arithmetic in Swift](https://github.com/Nadohs/Cast-Free-Arithmetic-in-Swift) - Cast-free arithmetic operations in Swift 2.0!
- [Cent](https://github.com/ankurp/Cent) - Extensions for Swift Standard Types and Classes.
- [CwlUtils](https://github.com/mattgallagher/CwlUtils) - A collection of Swift utilities as documented on cocoawithlove.com.
- [Dollar](https://github.com/ankurp/Dollar) - A functional tool-belt for Swift Language similar to Lo-Dash or Underscore.js in Javascript.
- [ExSwift](https://github.com/pNre/ExSwift) - A set of Swift extensions for standard types and classes. `Archived`
- [EZSwiftExtensions](https://github.com/Esqarrouth/EZSwiftExtensions) - How Swift standard types and classes were supposed to work. `UIKit`
- [Laconic](https://github.com/simplisticated/Laconic) - Short and clear expressions in Swift.
- [Mirror](https://github.com/kostiakoval/Mirror) - Swift objects Reflection API.
- [my-swift-projects](https://github.com/eonist/my-swift-projects) - An overview of my most relevant open-source projects on GitHub
- [QuickActions](https://github.com/ricardopereira/QuickActions) - Swift wrapper for iOS Home Screen Quick Actions (App Icon Shortcuts). `iOS`
- [Send-It-for-Slack](https://github.com/MoralAlberto/Send-It-for-Slack) - Add Slack functionality with this Safari Extension.
- [Solid](https://github.com/simplisticated/Solid) - New way to work with arrays in Swift.
- [Sugar](https://github.com/hyperoslo/Sugar) - Sugar is a sweetener for your Cocoa implementations. `iOS`
- [SwiftString](https://github.com/amayne/SwiftString) - SwiftString is a lightweight string extension for Swift.
- [SwiftyConfiguration](https://github.com/ykyouhei/SwiftyConfiguration) - Modern Swift API for Plist.
- [SwiftySwift](https://github.com/adeca/SwiftySwift) - Collection of useful extensions for Swift types and Cocoa objects.
- [Swiftz](https://github.com/typelift/Swiftz) - Functional programming in Swift.
- [UnchainedString](https://github.com/dunkelstern/UnchainedString) - Extensions for Swift Strings on Linux until the Foundation classes are up to speed. `Archived`
- [Verbose](https://github.com/simplisticated/Verbose) - Text generator written in Swift.
- [Versions](https://github.com/zenangst/Versions) - Helping you find inner peace when comparing version numbers in Swift.
