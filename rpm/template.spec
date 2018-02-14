Name:           ros-kinetic-pr2-mannequin-mode
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS pr2_mannequin_mode package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/pr2_mannequin_mode
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-pr2-controller-manager
Requires:       ros-kinetic-pr2-controllers-msgs
Requires:       ros-kinetic-trajectory-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-pr2-controller-manager
BuildRequires:  ros-kinetic-pr2-controllers-msgs
BuildRequires:  ros-kinetic-trajectory-msgs

%description
The pr2_mannequin_mode package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Feb 15 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 0.6.0-0
- Autogenerated by Bloom

