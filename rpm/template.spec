Name:           ros-kinetic-pr2-tuckarm
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS pr2_tuckarm package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_tuckarm
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-pr2-mechanism-msgs
Requires:       ros-kinetic-pr2-tuck-arms-action
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-trajectory-msgs
BuildRequires:  ros-kinetic-catkin

%description
Tucks the arms of the PR2 robot into a safe position for moving the base of the
robot. This also moves the arms out of the view of the tilting laser scanner, as
much as possible.

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

