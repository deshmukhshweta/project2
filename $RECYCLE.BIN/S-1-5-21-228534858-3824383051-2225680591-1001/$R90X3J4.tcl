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
    "-family {Segoe UI} -size 15 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI} -size 20 -weight bold -slant roman -underline 0 -overstrike 0" \
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
        -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 700x379+296+173
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "StockerRegistration "
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra38 \
        -borderwidth 10 -relief groove -background {#0cf4ae} -height 375 \
        -width 695 
    vTcl:DefineAlias "$top.fra38" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra38
    label $site_3_0.lab39 \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {Stocker Registration} 
    vTcl:DefineAlias "$site_3_0.lab39" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab40 \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -text Idno 
    vTcl:DefineAlias "$site_3_0.lab40" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab41 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text .............. 
    vTcl:DefineAlias "$site_3_0.lab41" "Label2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab42 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Name 
    vTcl:DefineAlias "$site_3_0.lab42" "Label2_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Phone 
    vTcl:DefineAlias "$site_3_0.lab43" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Password 
    vTcl:DefineAlias "$site_3_0.lab44" "Label2_4" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent46 \
        -background white -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent46" "stocker_name" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent47 \
        -background white -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent47" "stocker_phone" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent48 \
        -background white -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -show * 
    vTcl:DefineAlias "$site_3_0.ent48" "stocker_password" vTcl:WidgetProc "Toplevel1" 1
    frame $site_3_0.fra50 \
        -borderwidth 2 -relief groove -background {#141414} -height 355 \
        -width -5 
    vTcl:DefineAlias "$site_3_0.fra50" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but51 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#0cf4ae} -borderwidth 0 -command save_stocker \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font10,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Save 
    vTcl:DefineAlias "$site_3_0.but51" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {View Stocker } 
    vTcl:DefineAlias "$site_3_0.lab53" "Label1_8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab54 \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -text Idno 
    vTcl:DefineAlias "$site_3_0.lab54" "Label3" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent55 \
        -background white -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent55" "Entry2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but56 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#0cf4ae} -borderwidth 0 -command view_stocker \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font10,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text View 
    vTcl:DefineAlias "$site_3_0.but56" "Button2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab57 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Name 
    vTcl:DefineAlias "$site_3_0.lab57" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab58 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text ............... 
    vTcl:DefineAlias "$site_3_0.lab58" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab59 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Phone 
    vTcl:DefineAlias "$site_3_0.lab59" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab60 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text .............. 
    vTcl:DefineAlias "$site_3_0.lab60" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but61 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#0cf4ae} -borderwidth 0 -command delete_stocker \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font10,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Delete 
    vTcl:DefineAlias "$site_3_0.but61" "Button3" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab39 \
        -in $site_3_0 -x 23 -y 20 -width 269 -height 43 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab40 \
        -in $site_3_0 -x 21 -y 90 -width 58 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab41 \
        -in $site_3_0 -x 139 -y 102 -width 30 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab42 \
        -in $site_3_0 -x 12 -y 138 -width 90 -relwidth 0 -height 51 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab43 \
        -in $site_3_0 -x 9 -y 190 -width 100 -relwidth 0 -height 61 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab44 \
        -in $site_3_0 -x 10 -y 260 -width 120 -relwidth 0 -height 41 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent46 \
        -in $site_3_0 -x 136 -y 157 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent47 \
        -in $site_3_0 -x 135 -y 214 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent48 \
        -in $site_3_0 -x 137 -y 271 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.fra50 \
        -in $site_3_0 -x 345 -y 10 -width 1 -relwidth 0 -height 355 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but51 \
        -in $site_3_0 -x 217 -y 310 -width 78 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 388 -y 17 -width 269 -height 43 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 370 -y 82 -width 74 -relwidth 0 -height 51 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent55 \
        -in $site_3_0 -x 481 -y 99 -width 164 -height 20 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 528 -y 125 -width 60 -height 43 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 359 -y 175 -width 90 -height 51 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab58 \
        -in $site_3_0 -x 509 -y 177 -width 90 -height 51 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab59 \
        -in $site_3_0 -x 361 -y 233 -width 90 -height 51 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab60 \
        -in $site_3_0 -x 510 -y 232 -width 90 -height 51 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but61 \
        -in $site_3_0 -x 549 -y 309 -width 76 -height 43 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 1 -y 2 -width 695 -relwidth 0 -height 375 -relheight 0 \
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

