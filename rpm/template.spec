Name:           ros-indigo-parrot-arsdk
Version:        3.9.1
Release:        6%{?dist}
Summary:        ROS parrot_arsdk package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/parrot_arsdk
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  avahi-devel
BuildRequires:  curl
BuildRequires:  ffmpeg-devel
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  nasm
BuildRequires:  ncurses-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  unzip
BuildRequires:  yasm
BuildRequires:  zlib-devel

%description
Catkin wrapper for the official ARSDK from Parrot

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 25 2016 Mani Monajjemi <mmonajje@sfu.ca> - 3.9.1-6
- Autogenerated by Bloom

* Sat Jul 09 2016 Mani Monajjemi <mmonajje@sfu.ca> - 3.9.1-5
- Autogenerated by Bloom

* Thu Jul 07 2016 Mani Monajjemi <mmonajje@sfu.ca> - 3.9.1-4
- Autogenerated by Bloom

* Sat Jun 18 2016 Mani Monajjemi <mmonajje@sfu.ca> - 3.9.1-3
- Autogenerated by Bloom

* Thu Jun 16 2016 Mani Monajjemi <mmonajje@sfu.ca> - 3.9.1-2
- Autogenerated by Bloom

* Thu Jun 16 2016 Mani Monajjemi <mmonajje@sfu.ca> - 3.9.1-1
- Autogenerated by Bloom

* Sat Jun 11 2016 Mani Monajjemi <mmonajje@sfu.ca> - 3.9.1-0
- Autogenerated by Bloom

