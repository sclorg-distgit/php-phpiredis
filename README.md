This repository contains sources for RPMs that are used
to build Software Collections for CentOS by SCLo SIG.

This branch is for hiredis-devel, dependency of php-phpiredis
This package only build the static library

    cbs add-pkg    sclo6-sclo-php70-sclo-candidate --owner=sclo  hiredis
    cbs add-pkg    sclo7-sclo-php70-sclo-candidate --owner=sclo  hiredis
    cbs add-pkg    sclo7-sclo-php71-sclo-candidate --owner=sclo  hiredis
    cbs add-pkg    sclo7-sclo-php72-sclo-candidate --owner=sclo  hiredis
    cbs add-pkg    sclo7-sclo-php73-sclo-candidate --owner=sclo  hiredis

    build -bs *spec --define "dist .el7"
    cbs build      sclo7-sclo-php72-sclo-el7       <above>.src.rpm
    cbs tag-build  sclo7-sclo-php71-sclo-candidate <above build>
    cbs tag-build  sclo7-sclo-php70-sclo-candidate <above build>

    build -bs *spec --define "dist .el6"
    cbs build      sclo7-sclo-php70-sclo-el7       <above>.src.rpm
    cbs tag-build  sclo6-sclo-php70-sclo-candidate <above build>

    build -bs *spec --define "dist .el7"
    cbs build      sclo7-sclo-php72-sclo-el7       <above>.src.rpm
	=> hiredis-0.13.3-0.el7.1
