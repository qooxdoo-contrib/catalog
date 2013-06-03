===== Hijax =====
This is a small qooxdoo-based library that can be used to 'ajaxify' traditional
web pages.

Hijax intercepts click events on HTML links and form submit buttons, sending an 
XHR request to the server and replacing a specified part of the current page 
with content from the server's response document, avoiding the page flicker 
usually associated with loading a new page.

Since Hijax requires no changes to the HTML content or server backend, 
integrating it in an existing site is a fast and easy process.  

An additional benefit of this approach is that it provides graceful degradation, 
i.e. users with Javascript disabled in their browsers () can still use the site 
normally.

===== Demo =====
This contribution includes a small demo showing Hijax in action. 