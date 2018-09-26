Name:           ros-melodic-pr2-apps
Version:        0.6.1
Release:        0%{?dist}
Summary:        ROS pr2_apps package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_apps
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-pr2-app-manager
Requires:       ros-melodic-pr2-kinematics
Requires:       ros-melodic-pr2-mannequin-mode
Requires:       ros-melodic-pr2-position-scripts
Requires:       ros-melodic-pr2-teleop-general
Requires:       ros-melodic-pr2-tuckarm
BuildRequires:  ros-melodic-catkin

%description
Basic applications for the PR2 robot

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Sep 26 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 0.6.1-0
- Autogenerated by Bloom

