# XApp docs
This is an unofficial project that aims to bring information about how to create windows, basic apps and many other references regarding XApps, this in my few/little/minor experience that I have had with GTK and Python

As per [this page: ](https://linuxmint-developer-guide.readthedocs.io/en/latest/xapps.html) *"X-Apps is an idea to produce generic applications for traditional GTK desktop environments"*, as per creating this repository, the following Desktop Environments (or DE for short) are using GTK in their technologies

* GNOME
* Cinnamon
* Xfce
* Mate
* Budgie (as per versions 10 or below, newer might change or discard them eventually)
* Unity (though this one is using a very outdated version due to internal requirements as per my knowledge)

However GNOME, as the main user and developer of GTK as a whole, is starting to make their applications hard to integrate to other DE, and this is causing that the other group of DE not-GNOME have a hard time adapting to the changes being done there and integrating as intended. Linux Mint started this project in their personal effort to create a unified base that all GTK environments can benefit, as per the site: *"it makes no sense to develop 3 different text editors, 5 different calculators and so on. When we work on projects like these, we want to make it count. An improvement in the text editor shouldn’t benefit only one edition, it should benefit all of them"*

The core ideas for X-Apps are:

* To use modern toolkits and technologies (GTK3 for HiDPI support, gsettings etc..)
* To use traditional user interfaces (titlebars, menubars), though in this one it might depends on the XApp developed or being based on, since rebasing on newer versions of GNOME-specific apps might means losing the traditional interface (example, Pix)
* To work everywhere (to be generic, desktop-agnostic and distro-agnostic)
* To provide the functionality users already enjoy (or enjoyed in the past for distributions which already lost some functionality)
* To be backward-compatible (in order to work on as many distributions as possible)

Though the effort was started by Linux Mint, this doesn´t mean that the apps are specific to that distro, as per one of their ideas, many distros can benefit from what they do (Arch, Ubuntu, Fedora, openSUSE, etc.) and there are volunteers to port the apps to their respective distros as needed


**This is not intended to be a hating site or complaining to the GNOME project or any other DE project, any issue described here is my personal statement, and even then, it has been made in a neutral and peaceful manner to highlight facts and situations and not something as a "I hate (introduce the other DE here)", "Why the F&%^ do they intend to do this/not do this?", etc.**