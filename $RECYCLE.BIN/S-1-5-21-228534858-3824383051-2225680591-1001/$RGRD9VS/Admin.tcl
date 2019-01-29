#############################################################################
# Generated by PAGE version 4.13
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Courier New} -size 13 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI} -size 21 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font11
vTcl:font:add_font \
    "-family {Segoe UI} -size 16 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top37
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.fra38
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#79d8c8} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 487x337+384+154
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1362 741
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Admin Login"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra38 \
        -borderwidth 14 -relief groove -background {#d820d8} -height 315 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 465 
    vTcl:DefineAlias "$top.fra38" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra38
    label $site_3_0.lab39 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d820d8} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Admin Login} 
    vTcl:DefineAlias "$site_3_0.lab39" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab40 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d820d8} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Username 
    vTcl:DefineAlias "$site_3_0.lab40" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab42 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d820d8} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Password 
    vTcl:DefineAlias "$site_3_0.lab42" "Admin_paas" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent43 \
        -background white -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent43" "Admin_username" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent44 \
        -background white -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -show * 
    vTcl:DefineAlias "$site_3_0.ent44" "Admin_password" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but45 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d820d8} -borderwidth 0 -command Admin_validation \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Login 
    vTcl:DefineAlias "$site_3_0.but45" "Admin_Button" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but38 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d820d8} -borderwidth 0 -command Admin_Cancel \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Cancel 
    vTcl:DefineAlias "$site_3_0.but38" "Admin_Button_1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab39 \
        -in $site_3_0 -x 131 -y 18 -width 214 -relwidth 0 -height 41 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab40 \
        -in $site_3_0 -x 23 -y 93 -width 114 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab42 \
        -in $site_3_0 -x 22 -y 137 -width 114 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent43 \
        -in $site_3_0 -x 143 -y 94 -width 184 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent44 \
        -in $site_3_0 -x 144 -y 139 -width 184 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 134 -y 190 -width 87 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but38 \
        -in $site_3_0 -x 248 -y 191 -width 87 -height 34 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 10 -y 10 -width 465 -relwidth 0 -height 315 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

