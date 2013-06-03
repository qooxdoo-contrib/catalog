===== qooxdoo =====

<note>
Setting up this directory as explained below is NOT required when simply //using// 
contributions in your custom application. For information on how-to easily 
include projects from qooxdoo-contrib into your apps please consult the manual.
</note>

This directory is an integral part of the qooxdoo-contrib development 
infrastructure. In order to generate demo versions of the various projects in a 
qooxdoo-contrib checkout the corresponding SDK versions (or SVN trunk) of the 
qooxdoo framework need to be referenced. 

To allow for a single, unified way of setting up the configuration across all 
contributions this directory is intended to contain file system links to the 
required qooxdoo SDK versions (or SVN trunk). Of course, creating such links 
strongly depend on the operating system you use. Also see the 
[[http://en.wikipedia.org/wiki/Symbolic_link|wikipedia article]] on symbolic 
links.

Please follow the instructions below to manage symbolic links to the directories 
of the qooxdoo SDKs (or SVN checkouts).


==== Windows ====

For the following examples it is assumed you have a qooxdoo-contrib checkout at 
C:\workspace\qooxdoo-contrib . Additionally you have extracted a qooxdoo SDK 
archive (lets say 0.8.2) to C:\workspace\qooxdoo-0.8.2-sdk and you checked out 
the SVN trunk of qooxdoo to C:\workspace\qooxdoo.trunk .


=== Windows (Vista and newer) ===

Newer versions of Microsoft Windows (i.e. Vista and above) support the creation 
of symbolic links with the built-in command line utility mklink:

<code>
  mklink /d "C:\workspace\qooxdoo-contrib\qooxdoo\0.8.2" \
    "C:\workspace\qooxdoo-0.8.2-sdk"

  mklink /d "C:\workspace\qooxdoo-contrib\qooxdoo\trunk" \
    "C:\workspace\qooxdoo.trunk"
</code>

To remove an existing link to a directory:

<code>
  rmdir /s /q "C:\workspace\qooxdoo-contrib\qooxdoo\0.8.2"  
  rmdir /s /q "C:\workspace\qooxdoo-contrib\qooxdoo\trunk"
</code>


=== Windows (XP and older) ===

Older versions of Microsoft Windows (XP and below) require an additional utility 
to create symbolic links. One such utility is linkd.exe from the 
[[http://www.microsoft.com/downloads/details.aspx?FamilyID=9d467a69-57ff-4ae7-96ee-b18c4790cffd&DisplayLang=en|Window 2003 
Resource Tools Kit ]] or the more powerful [[http://www.microsoft.com/technet/sysinternals/FileAndDisk/Junction.mspx|junction.exe]].

Change to the qooxdoo directory of your qooxdoo-contrib checkout and create 
symbolic links as shown here:

<code>
  cd C:\workspace\qooxdoo-contrib\qooxdoo

  junction.exe "0.8.2" "C:\workspace\qooxdoo-0.8.2-sdk"
  junction.exe "trunk" "C:\workspace\qooxdoo.trunk"
</code>

To remove an existing link to a directory:

<code>
  junction.exe -d "0.8.2"
  junction.exe -d "trunk"
</code>


=== Cygwin ===

Link handling should be equivalent to Linux.


==== Linux ====

For the following examples it is assumed you have a qooxdoo-contrib checkout at 
/opt/workspace/qooxdoo-contrib . Additionally you have extracted a qooxdoo SDK 
archive (lets say 0.8.2) to /opt/workspace/qooxdoo-0.8.2-sdk and you checked out 
the SVN trunk of qooxdoo to /opt/workspace/qooxdoo.trunk .

Change to the qooxdoo directory of your qooxdoo-contrib checkout and create 
symbolic links as shown here:

<code>
  cd /opt/workspace/qooxdoo-contrib/qooxdoo
  ln -s /opt/workspace/qooxdoo-0.8.2-sdk 0.8.2
  ln -s /opt/workspace/qooxdoo.trunk trunk
</code>

To remove an existing link to a directory:

<code>
  rm "0.8.2"
  rm "trunk"
</code>

==== Mac ====

Link handling should be equivalent to Linux.


==== Legacy information (up to 0.7.x) ====

<note>
The information below refers to legacy versions of qooxdoo and 
qooxdoo-contrib and may not apply to releases 0.8.x and above.
</note>

This directory can be manually populated by specific qooxdoo SDK versions that 
are required to build certain contributions.

For instance, execute a "make download-0.7.3" in order to download the 0.7.3 
framework SDK into this directory.
