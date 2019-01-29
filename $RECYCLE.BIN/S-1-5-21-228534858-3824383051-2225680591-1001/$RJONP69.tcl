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
    "-family {Courier New} -size 13 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font11
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
    wm geometry $top 713x399+297+118
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
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra38 \
        -borderwidth 2 -relief groove -background {#0cf4ae} -height 385 \
        -width 695 
    vTcl:DefineAlias "$top.fra38" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra38
    frame $site_3_0.fra39 \
        -borderwidth 2 -relief groove -background {#0f0f0f} -height 385 \
        -width -5 
    vTcl:DefineAlias "$site_3_0.fra39" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab40 \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -text {Dispatcher Registration} 
    vTcl:DefineAlias "$site_3_0.lab40" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab41 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text { View Dispatcher } 
    vTcl:DefineAlias "$site_3_0.lab41" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab42 \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -text Idno 
    vTcl:DefineAlias "$site_3_0.lab42" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text ......... 
    vTcl:DefineAlias "$site_3_0.lab43" "Label2_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Name 
    vTcl:DefineAlias "$site_3_0.lab44" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Phone 
    vTcl:DefineAlias "$site_3_0.lab45" "Label2_4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Password 
    vTcl:DefineAlias "$site_3_0.lab46" "Label2_5" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent47 \
        -background white -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent47" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent48 \
        -background white -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent48" "Entry1_6" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent49 \
        -background white -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent49" "Entry1_7" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but50 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#0cf4ae} -borderwidth 0 -command save_dispatcher \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font10,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Save 
    vTcl:DefineAlias "$site_3_0.but50" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab51 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Idno 
    vTcl:DefineAlias "$site_3_0.lab51" "Label2_8" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent52 \
        -background white -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent52" "Entry1_7" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but53 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#0cf4ae} -borderwidth 0 -command show_dispatcher \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font10,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Show 
    vTcl:DefineAlias "$site_3_0.but53" "Button1_8" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab54 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Name 
    vTcl:DefineAlias "$site_3_0.lab54" "Label2_4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab55 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Phone 
    vTcl:DefineAlias "$site_3_0.lab55" "Label2_5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab56 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text ......... 
    vTcl:DefineAlias "$site_3_0.lab56" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab57 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#0cf4ae} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text ......... 
    vTcl:DefineAlias "$site_3_0.lab57" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but58 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#0cf4ae} -borderwidth 0 -command delete_dispatcher \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font10,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Delete 
    vTcl:DefineAlias "$site_3_0.but58" "Button1_4" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.fra39 \
        -in $site_3_0 -x 360 -y 0 -width -5 -relwidth 0 -height 385 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab40 \
        -in $site_3_0 -x 30 -y 10 -anchor nw -bordermode ignore 
    place $site_3_0.lab41 \
        -in $site_3_0 -x 375 -y 12 -width 310 -height 43 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab42 \
        -in $site_3_0 -x 19 -y 86 -width 58 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab43 \
        -in $site_3_0 -x 124 -y 95 -width 60 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab44 \
        -in $site_3_0 -x 10 -y 134 -width 80 -relwidth 0 -height 51 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 8 -y 206 -width 90 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 3 -y 253 -width 120 -relwidth 0 -height 51 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent47 \
        -in $site_3_0 -x 129 -y 151 -width 162 -relwidth 0 -height 32 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent48 \
        -in $site_3_0 -x 128 -y 207 -width 164 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent49 \
        -in $site_3_0 -x 128 -y 265 -width 164 -relwidth 0 -height 30 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but50 \
        -in $site_3_0 -x 169 -y 320 -width 97 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 383 -y 89 -width 58 -height 34 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent52 \
        -in $site_3_0 -x 480 -y 93 -width 164 -height 30 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but53 \
        -in $site_3_0 -x 520 -y 140 -width 97 -height 34 -anchor nw \
        -bordermode inside 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 374 -y 198 -width 80 -height 51 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 371 -y 261 -width 90 -height 31 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 501 -y 213 -width 60 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 501 -y 267 -width 60 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but58 \
        -in $site_3_0 -x 570 -y 310 -width 97 -height 34 -anchor nw \
        -bordermode inside 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 10 -y 6 -width 695 -relwidth 0 -height 385 -relheight 0 \
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

