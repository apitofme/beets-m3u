# beets-m3u
A beets plugin to generate M3U playlists
___
**Proposal for new Beets plugin**

_Name:_	&nbsp; m3ulist

_Desc:_	&nbsp; A plugin to create m3u playlists for ...
- albums during import operations
- albums already in database (auto-gen one / some / all)
- all items returned by a custom search query

_Details:_
The plugin should ...
- offer relative or absolute file paths in playlists
- allow saving of playlist file to different locations
  (e.g. album folder, library-level folder or custom directory)
- optionally (auto) generate a playlist when an album is imported
- provide a CLI to create playlist files for existing library entities,
  this should include albums and custom compilations of singletons

_Considerations:_
- optionally include the UTF-8 BOM for the M3U8 format?
- support other playlist formats (e.g. PLS)?
- limit the number of items allowed per playlist!
  (or at least per generate operation?)
- provide ability to append items to an existing playlist file?
- update playlist files when items are changed, preferably on-demand
  (i.e. search for playlist items (per playlist) and update as required)
- provide some means to test which albums do/don't have a playlist
  associated with them? (e.g. create a reference in the database!)
