#
# Example spec file for cdplayer app...
#
Summary: Test RPM!
Name: testrpm
Version: 1.0
Release: 6
Group: Applications/Sound
License: GPL
Source: test.tgz
Source1: common.inc
Vendor: Eason
Packager: Eason 
%include %{SOURCE1}

%description
This is a test RPM

%pre
echo pre $1
%supervisord -b hi kk
%dump

%post
echo post $1

%preun
echo preun $1

%postun
echo postun $1

%files
