/*global List */
q.ready(function() {
    'use strict';

    // @namespace
    var contrib = {
      getContribTmpl: function(data) {
        return q.template.get('ctb-overview-tmpl', {
          contribs: data,
          amount: data.length
        })[0].innerHTML;
      },

      initCtbOverview: function() {
        var listInit = true;

        var list = new List('contribs', {
          valueNames: [
            'ctb-name',
            'ctb-shortdesc',
            'ctb-category',
            'ctb-authors',
            'ctb-versions',
            'ctb-qxversions',
            'ctb-license'
          ],
          indexAsync: true
        });

        list.on('updated', function () {
          if (listInit) {
            listInit = false;
          }

          if (list.matchingItems.length > 0) {
            q('.table thead').show();
            q('.search-notfound').hide();
          } else if (list.matchingItems.length === 0) {
            q('.table thead').hide();
            q('.search-notfound').show();
          }
        });
      },

      initCtbDetail: function() {
        q('.list').on('click', function(e) {
          var origin = e.getTarget();
          var trElems = q(origin).getAncestorsUntil('.list', 'tr');

          if (trElems.length === 1) {
            var ctbName = trElems.getFirst().getData('ctb-name');
            // push list-{name} into history for back button support
            window.location.hash = 'list-'+ctbName;
            window.location.hash = '#'+ctbName;
          }
        });
      }
    };

    var render = function(data, ctx) {
      q('.contribs-loading').hide();

      var showOverview = function() {
        q('.info .overview').removeClass('hidden');
        q('.info .detail').addClass('hidden');
        q('#contribs').empty().append(ctx.getContribTmpl(data)).find('.search').show();

        ctx.initCtbOverview();
        ctx.initCtbDetail();
      };

      var showDetail = function(data) {
        var curHash = window.location.hash;
        var l = data.length;
        var detailTmpl;

        while (l--) {
          if (curHash === '#'+data[l].name) {
            detailTmpl = q.template.get('ctb-detail-tmpl', data[l])[0].innerHTML;

            q('.info .overview').addClass('hidden');
            q('.info .detail').removeClass('hidden').find('a').setAttribute('href', '#list-'+data[l].name);
            q('#contribs').empty().append(detailTmpl);
          }
        }

        if (!detailTmpl) {
          showOverview();
        }
      }.bind(this, data);

      var evaluateHash = function () {
        var curHash = window.location.hash;
        if (curHash === "" || curHash.indexOf('#list') === 0) {
          showOverview();
          var trElem = q(curHash);
          if (trElem && trElem[0]) {
            trElem[0].scrollIntoView();
          }
        } else {
          showDetail();
          window.scrollTo(0, 0);
        }
      };

      evaluateHash();
      window.onhashchange = evaluateHash;
    };

    var IDX_URL = 'json/contribindex.json';
    var xhr = q.io.xhr(IDX_URL);

    xhr.on('load', function(callback, xhr) {
      if (xhr.status === 200 && xhr.responseText) {
        callback(JSON.parse(xhr.responseText), contrib);
      } else {
        q('.contribs-loading p').setAttribute("text", 'Failed to load contribs list :(');
      }
    }.bind(contrib, render));

    xhr.on('error', function() {
      q('.contribs-loading p').setAttribute("text", 'Failed to load contribs list :(');
    });

    xhr.send();
});
