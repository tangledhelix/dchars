  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>dchars/0.3.8/dchars/languages/bod/dstring.py at 223edf6bde0d6c8a1475971375271f82674571b3 · suizokukan/dchars</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/modules/logos_page/Octocat.png">
    <link rel="assets" href="https://a248.e.akamai.net/assets.github.com/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="3998078" name="octolytics-actor-id" /><meta content="suizokukan" name="octolytics-actor-login" /><meta content="1b97d94afd4bbfaba9870e2d819bc9fd3d6d417d47e92c338e8db94d5c7a838f" name="octolytics-actor-hash" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="JuSGFeLXQes4GbqgvXQALWAimqljzWfJHCx2QzqShCk=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-52c7f5d250c57ca1380f2a5703d96d015d5eb533.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-58b10e96bcdc3e0d5ea328ffcd01e36e2e8fd07e.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-4c434fa1705bf526e191eec0cd8fab1a5ce3e326.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-c9ee6873d0b9bc74d5f353bd006a81aa3efc29b3.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="9a05a1423af26d07af36db19fa49a2c8">

        <link data-pjax-transient rel='permalink' href='/suizokukan/dchars/blob/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars/languages/bod/dstring.py'>
    <meta property="og:title" content="dchars"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/suizokukan/dchars"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/8e0379710f523b8ef48a1d74fea00430?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="dchars - D(etailed) char(acter)s for Biblical Hebrew, Ancient Greek, Sanskrit, Latin and Tibetan"/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="suizokukan/dchars"/>

    <meta name="description" content="dchars - D(etailed) char(acter)s for Biblical Hebrew, Ancient Greek, Sanskrit, Latin and Tibetan" />


    <meta content="3998078" name="octolytics-dimension-user_id" /><meta content="suizokukan" name="octolytics-dimension-user_login" /><meta content="10844644" name="octolytics-dimension-repository_id" /><meta content="suizokukan/dchars" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="10844644" name="octolytics-dimension-repository_network_root_id" /><meta content="suizokukan/dchars" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/suizokukan/dchars/commits/223edf6bde0d6c8a1475971375271f82674571b3.atom" rel="alternate" title="Recent Commits to dchars:223edf6bde0d6c8a1475971375271f82674571b3" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob linux vis-public env-production  ">
    <div id="wrapper">

      
      
      

      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    <div class="divider-vertical"></div>

      <a href="/notifications" class="notification-indicator tooltipped downwards" title="You have no unread notifications">
    <span class="mail-status all-read"></span>
  </a>
  <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey=" s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    data-username="suizokukan"
      data-repo="suizokukan/dchars"
      data-branch=""
      data-sha="f07845057ee20083092e05ca34f4b70edff13bc1"
  >

    <input type="hidden" name="nwo" value="suizokukan/dchars" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
            <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    

  

    <ul id="user-links">
      <li>
        <a href="/suizokukan" class="name">
          <img height="20" src="https://secure.gravatar.com/avatar/8e0379710f523b8ef48a1d74fea00430?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /> suizokukan
        </a>
      </li>

        <li>
          <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo">
            <span class="octicon octicon-repo-create"></span>
          </a>
        </li>

        <li>
          <a href="/settings/profile" id="account_settings"
            class="tooltipped downwards"
            title="Account settings ">
            <span class="octicon octicon-tools"></span>
          </a>
        </li>
        <li>
          <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out">
            <span class="octicon octicon-log-out"></span>
          </a>
        </li>

    </ul>


<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-list-unordered"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="suizokukan/dchars">This repository</span>
    </li>
    <li>
      <a href="/suizokukan/dchars/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
      <li>
        <a href="/suizokukan/dchars/settings/collaboration"><span class="octicon octicon-person-add"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

      




            <div class="global-notices">
      <div class="flash-global">
        <div class="container">
            <a href="/users/suizokukan/enable_repository_next?nwo=suizokukan%2Fdchars" class="button minibutton flash-action blue" data-method="post">Enable Repository Next</a>

            <h2>Hey there, would you like to enable our new repository design?</h2>
            <p>We&rsquo;ve been working hard making a <a href="https://github.com/blog/1529-repository-next">faster, better repository experience</a> and we&rsquo;d love to share it with you.</p>
        </div>
      </div>
    </div>
    <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">

    <li class="nspr">
      <a href="/suizokukan/dchars/pull/new/223edf6bde0d6c8a1475971375271f82674571b3" class="button minibutton btn-pull-request" icon_class="octicon-git-pull-request"><span class="octicon octicon-git-pull-request"></span>Pull Request</a>
    </li>

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="JuSGFeLXQes4GbqgvXQALWAimqljzWfJHCx2QzqShCk=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="10844644" />

    <div class="select-menu js-menu-container js-select-menu">
      <span class="minibutton select-menu-button  js-menu-target">
        <span class="js-select-button">
          <span class="octicon octicon-eye-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

    <li class="js-toggler-container js-social-container starring-container ">
      <a href="/suizokukan/dchars/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star-delete"></span>
        <span class="text">Unstar</span>
      </a>
      <a href="/suizokukan/dchars/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star"></span>
        <span class="text">Star</span>
      </a>
      <a class="social-count js-social-count" href="/suizokukan/dchars/stargazers">0</a>
    </li>

        <li>
          <a href="/suizokukan/dchars/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span>
            <span class="text">Fork</span>
          </a>
          <a href="/suizokukan/dchars/network" class="social-count">0</a>
        </li>


</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-octicon octicon-repo"></span>
                <span class="author vcard">
                  <a href="/suizokukan" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">suizokukan</span>
                  </a></span> /
                <strong><a href="/suizokukan/dchars" class="js-current-repository">dchars</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/suizokukan/dchars/pulse" class="js-selected-navigation-item " data-selected-links="pulse /suizokukan/dchars/pulse" rel="nofollow"><span class="octicon octicon-pulse"></span></a></li>
    <li><a href="/suizokukan/dchars" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /suizokukan/dchars">Code</a></li>
    <li><a href="/suizokukan/dchars/network" class="js-selected-navigation-item " data-selected-links="repo_network /suizokukan/dchars/network">Network</a></li>
    <li><a href="/suizokukan/dchars/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /suizokukan/dchars/pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/suizokukan/dchars/issues" class="js-selected-navigation-item " data-selected-links="repo_issues /suizokukan/dchars/issues">Issues <span class='counter'>0</span></a></li>

      <li><a href="/suizokukan/dchars/wiki" class="js-selected-navigation-item " data-selected-links="repo_wiki /suizokukan/dchars/wiki">Wiki</a></li>


    <li><a href="/suizokukan/dchars/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /suizokukan/dchars/graphs">Graphs</a></li>

      <li>
        <a href="/suizokukan/dchars/settings">Settings</a>
      </li>

  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/suizokukan/dchars/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /suizokukan/dchars/tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="">
        <span class="octicon octicon-tag"></span>
        <i>tree:</i>
        <span class="js-select-button">223edf6bde</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/suizokukan/dchars/blob/master/0.3.8/dchars/languages/bod/dstring.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <form accept-charset="UTF-8" action="/suizokukan/dchars/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="JuSGFeLXQes4GbqgvXQALWAimqljzWfJHCx2QzqShCk=" /></div>

                <span class="octicon octicon-git-branch-create select-menu-item-icon"></span>
                <div class="select-menu-item-text">
                  <h4>Create branch: <span class="js-new-item-name"></span></h4>
                  <span class="description">from ‘223edf6bde0d6c8a1475971375271f82674571b3’</span>
                </div>
                <input type="hidden" name="name" id="name" class="js-new-item-value">
                <input type="hidden" name="branch" id="branch" value="223edf6bde0d6c8a1475971375271f82674571b3" />
                <input type="hidden" name="path" id="branch" value="0.3.8/dchars/languages/bod/dstring.py" />
              </form> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/suizokukan/dchars" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /suizokukan/dchars">Files</a></li>
    <li><a href="/suizokukan/dchars/commits/" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /suizokukan/dchars/commits/">Commits</a></li>
    <li><a href="/suizokukan/dchars/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /suizokukan/dchars/branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:4b9905c9c6ad7faf5b6a2accd5cee620 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:4b9905c9c6ad7faf5b6a2accd5cee620 -->

<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <a href="/suizokukan/dchars/find/223edf6bde0d6c8a1475971375271f82674571b3" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>

        <div class="breadcrumb">
          <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/suizokukan/dchars/tree/223edf6bde0d6c8a1475971375271f82674571b3" class="js-slide-to" data-branch="223edf6bde0d6c8a1475971375271f82674571b3" data-direction="back" itemscope="url" rel="nofollow"><span itemprop="title">dchars</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/suizokukan/dchars/tree/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8" class="js-slide-to" data-branch="223edf6bde0d6c8a1475971375271f82674571b3" data-direction="back" itemscope="url" rel="nofollow"><span itemprop="title">0.3.8</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/suizokukan/dchars/tree/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars" class="js-slide-to" data-branch="223edf6bde0d6c8a1475971375271f82674571b3" data-direction="back" itemscope="url" rel="nofollow"><span itemprop="title">dchars</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/suizokukan/dchars/tree/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars/languages" class="js-slide-to" data-branch="223edf6bde0d6c8a1475971375271f82674571b3" data-direction="back" itemscope="url" rel="nofollow"><span itemprop="title">languages</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/suizokukan/dchars/tree/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars/languages/bod" class="js-slide-to" data-branch="223edf6bde0d6c8a1475971375271f82674571b3" data-direction="back" itemscope="url" rel="nofollow"><span itemprop="title">bod</span></a></span><span class="separator"> / </span><strong class="final-path">dstring.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="0.3.8/dchars/languages/bod/dstring.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/suizokukan/dchars/contributors/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars/languages/bod/dstring.py">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/suizokukan/dchars/blob/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars/languages/bod/dstring.py" data-title="dchars/0.3.8/dchars/languages/bod/dstring.py at 223edf6bde0d6c8a1475971375271f82674571b3 · suizokukan/dchars · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>420 lines (343 sloc)</span>
                <span>17.353 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/suizokukan/dchars/raw/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars/languages/bod/dstring.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/suizokukan/dchars/blame/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars/languages/bod/dstring.py" class="button minibutton ">Blame</a>
                  <a href="/suizokukan/dchars/commits/223edf6bde0d6c8a1475971375271f82674571b3/0.3.8/dchars/languages/bod/dstring.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python3</span></div><div class='line' id='LC2'><span class="c"># -*- coding: utf-8 -*-</span></div><div class='line' id='LC3'><span class="c">################################################################################</span></div><div class='line' id='LC4'><span class="c">#    DChars Copyright (C) 2012 Suizokukan</span></div><div class='line' id='LC5'><span class="c">#    Contact: suizokukan _A.T._ orange dot fr</span></div><div class='line' id='LC6'><span class="c">#</span></div><div class='line' id='LC7'><span class="c">#    This file is part of DChars.</span></div><div class='line' id='LC8'><span class="c">#    DChars is free software: you can redistribute it and/or modify</span></div><div class='line' id='LC9'><span class="c">#    it under the terms of the GNU General Public License as published by</span></div><div class='line' id='LC10'><span class="c">#    the Free Software Foundation, either version 3 of the License, or</span></div><div class='line' id='LC11'><span class="c">#    (at your option) any later version.</span></div><div class='line' id='LC12'><span class="c">#</span></div><div class='line' id='LC13'><span class="c">#    DChars is distributed in the hope that it will be useful,</span></div><div class='line' id='LC14'><span class="c">#    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></div><div class='line' id='LC15'><span class="c">#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></div><div class='line' id='LC16'><span class="c">#    GNU General Public License for more details.</span></div><div class='line' id='LC17'><span class="c">#</span></div><div class='line' id='LC18'><span class="c">#    You should have received a copy of the GNU General Public License</span></div><div class='line' id='LC19'><span class="c">#    along with DChars.  If not, see &lt;http://www.gnu.org/licenses/&gt;.</span></div><div class='line' id='LC20'><span class="c">################################################################################</span></div><div class='line' id='LC21'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC22'><span class="sd">    ❏DChars❏ : dchars/languages/bod/dstring.py</span></div><div class='line' id='LC23'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><span class="kn">import</span> <span class="nn">pickle</span></div><div class='line' id='LC26'><span class="kn">import</span> <span class="nn">os.path</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'><span class="c"># problem with Pylint :</span></div><div class='line' id='LC29'><span class="c"># pylint: disable=E0611</span></div><div class='line' id='LC30'><span class="c"># many errors like &quot;No name &#39;extensions&#39; in module &#39;dchars&#39;&quot;</span></div><div class='line' id='LC31'><span class="kn">from</span> <span class="nn">dchars.utilities.triggerlist</span> <span class="kn">import</span> <span class="n">TriggerList</span></div><div class='line' id='LC32'><span class="kn">from</span> <span class="nn">dchars.errors.errors</span> <span class="kn">import</span> <span class="n">DCharsError</span></div><div class='line' id='LC33'><span class="kn">from</span> <span class="nn">dchars.languages.bod.dcharacter</span> <span class="kn">import</span> <span class="n">DCharacterBOD</span></div><div class='line' id='LC34'><span class="kn">from</span> <span class="nn">dchars.languages.bod.symbols</span> <span class="kn">import</span> <span class="n">TSHEG_SYMBOL</span><span class="p">,</span> <span class="n">SPACE_SYMBOL</span></div><div class='line' id='LC35'><span class="kn">from</span> <span class="nn">dchars.dstring</span> <span class="kn">import</span> <span class="n">DStringMotherClass</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="kn">import</span> <span class="nn">dchars.languages.bod.buffer</span> <span class="kn">as</span> <span class="nn">bod_buffer</span></div><div class='line' id='LC38'><span class="kn">import</span> <span class="nn">dchars.languages.bod.transliterations.ewts_buffer</span> <span class="kn">as</span> <span class="nn">ewts_buffer</span></div><div class='line' id='LC39'><span class="kn">import</span> <span class="nn">dchars.languages.bod.internalstructure</span> <span class="kn">as</span> <span class="nn">istruct</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'><span class="c">################################################################################</span></div><div class='line' id='LC42'><span class="c"># known transliterations :</span></div><div class='line' id='LC43'><span class="c">################################################################################</span></div><div class='line' id='LC44'><span class="kn">import</span> <span class="nn">dchars.languages.bod.transliterations.ewts</span> <span class="kn">as</span> <span class="nn">trans_ewts</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'><span class="kn">import</span> <span class="nn">dchars.languages.bod.transliterations.bodsan</span> <span class="kn">as</span> <span class="nn">trans_bodsan</span></div><div class='line' id='LC47'><br/></div><div class='line' id='LC48'><span class="c">################################################################################</span></div><div class='line' id='LC49'><span class="c"># substitutions :</span></div><div class='line' id='LC50'><span class="c">################################################################################</span></div><div class='line' id='LC51'><span class="n">INIT_FROM_STR__SUBSTITUTIONS</span> <span class="o">=</span> <span class="p">(</span></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># ཀྵ -&gt; ཀྵ</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F40</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB5</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F69</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># གྷ -&gt; གྷ</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F42</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F43</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># ཌྷ -&gt; ཌྷ</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F4C</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F4D</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># དྷ -&gt; དྷ</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F51</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F52</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># བྷ -&gt; བྷ</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F56</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F57</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># ཛྷ -&gt; ཛྷ</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F5B</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F5C</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ཱི -&gt;  ཱི</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F71</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F72</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F73</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ཱུ -&gt;  ཱུ</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F71</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F74</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F75</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ཱྀ -&gt; ཱྀ</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F71</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F80</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F81</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ྐྵ -&gt;  ྐྵ</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F90</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB5</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB9</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ྒྷ -&gt;  ྒྷ</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F92</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F93</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ྜྷ -&gt;  ྜྷ</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F9C</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F9D</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ྡྷ -&gt;  ྡྷ</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FA1</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FA2</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ྦྷ -&gt;  ྦྷ</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FA6</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FA7</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ྫྷ -&gt;  ྫྷ</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FAB</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB7</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FAC</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ྲྀ -&gt;  ྲྀ</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB2</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F80</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F76</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#  ླྀ -&gt;  ླྀ</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0FB3</span><span class="p">)</span> <span class="o">+</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F80</span><span class="p">),</span> <span class="nb">chr</span><span class="p">(</span><span class="mh">0x0F78</span><span class="p">)</span> <span class="p">),</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC88'><br/></div><div class='line' id='LC89'><span class="c">################################################################################</span></div><div class='line' id='LC90'><span class="k">class</span> <span class="nc">DStringBOD</span><span class="p">(</span><span class="n">DStringMotherClass</span><span class="p">):</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC92'><span class="sd">        class DStringBOD</span></div><div class='line' id='LC93'><br/></div><div class='line' id='LC94'><span class="sd">        DO NOT CREATE A DStringBOD object directly but use instead the</span></div><div class='line' id='LC95'><span class="sd">        dchars.py::new_dstring() function.</span></div><div class='line' id='LC96'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC97'><br/></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">trans__get_transliteration</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;ewts&quot;</span>   <span class="p">:</span> <span class="n">trans_ewts</span><span class="o">.</span><span class="n">dstring__get_translit_str</span><span class="p">,</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;bodsan&quot;</span> <span class="p">:</span> <span class="n">trans_bodsan</span><span class="o">.</span><span class="n">dstring__get_translit_str</span><span class="p">,</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC102'><br/></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">trans__get_intstruct_from_trans_str</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;ewts&quot;</span>   <span class="p">:</span> <span class="n">trans_ewts</span><span class="o">.</span><span class="n">get_intstruct_from_trans_str</span><span class="p">,</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;bodsan&quot;</span> <span class="p">:</span> <span class="n">trans_bodsan</span><span class="o">.</span><span class="n">get_intstruct_from_trans_str</span><span class="p">,</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">str_src</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC112'><span class="sd">                DStringBOD.__init__</span></div><div class='line' id='LC113'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">DStringMotherClass</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">alert_function</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">alert__dchars_have_changed</span><span class="p">)</span></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># internal structure(s) corresponding to self&#39;s content :</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Should be initialized by self.init_from_transliteration() or</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># by self.init_from_str().</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">are_the_options_valid</span><span class="p">()</span></div><div class='line' id='LC122'><br/></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Pylint can&#39;t know that &lt;self&gt; has an &#39;options&#39; member</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># created when &lt;self&gt; has been initialized by new_dstring() :</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># pylint: disable=E1101</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># -&gt; &quot;Instance of &#39;DStringBOD&#39; has no &#39;options&#39; member&quot;</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">[</span><span class="s">&quot;look up in the buffers&quot;</span><span class="p">]</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">bod_buffer</span><span class="o">.</span><span class="n">BUFFER_LOADED</span><span class="p">:</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bod_buffer</span><span class="o">.</span><span class="n">BUFFER_LOADED</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">load_the_buffers</span><span class="p">()</span></div><div class='line' id='LC129'><br/></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">str_src</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">init_from_str</span><span class="p">(</span><span class="n">str_src</span><span class="p">)</span></div><div class='line' id='LC132'><br/></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__setattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC136'><span class="sd">                DStringBOD.__setattr__</span></div><div class='line' id='LC137'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we set the attribute :</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">object</span><span class="o">.</span><span class="n">__setattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we check the validity of the option(s) :</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="s">&quot;options&quot;</span><span class="p">:</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">are_the_options_valid</span><span class="p">()</span></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC152'><span class="sd">                DStringBOD.__str__</span></div><div class='line' id='LC153'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">char</span><span class="p">)</span> <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">])</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">alert__dchars_have_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC159'><span class="sd">                DStringBod.alert__dchars_have_changed</span></div><div class='line' id='LC160'><br/></div><div class='line' id='LC161'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span> <span class="o">=</span> <span class="n">istruct</span><span class="o">.</span><span class="n">get_intstructures_from_dstring</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">alert__istructs_have_changed</span><span class="p">()</span></div><div class='line' id='LC164'><br/></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">alert__istructs_have_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC168'><span class="sd">                DStringBOD.alert__istructs_have_changed</span></div><div class='line' id='LC169'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">alert_off</span><span class="p">()</span></div><div class='line' id='LC171'><br/></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span></div><div class='line' id='LC173'><br/></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;istructs&#39;</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__dict__</span><span class="p">:</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">get_the_corresponding_dchars</span><span class="p">(</span><span class="n">dcharactertype</span><span class="o">=</span><span class="n">DCharacterBOD</span><span class="p">,</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span><span class="o">=</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">char</span> <span class="p">)</span></div><div class='line' id='LC178'><br/></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">alert_on</span><span class="p">()</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">are_the_options_valid</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC184'><span class="sd">                DStringBOD.are_the_options_valid</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'><span class="sd">                Raise an error if self.options isn&#39;t correctly initialized.</span></div><div class='line' id='LC187'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC188'><br/></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># options[&quot;expected_structure&quot;]</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC192'><br/></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Pylint can&#39;t know that &lt;self&gt; has an &#39;options&#39; member</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># created when &lt;self&gt; has been initialized by new_dstring() :</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># pylint: disable=E1101</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># -&gt; &quot;Instance of &#39;DStringBOD&#39; has no &#39;options&#39; member&quot;</span></div><div class='line' id='LC197'><br/></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">expected_structure</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">[</span><span class="s">&quot;expected structure&quot;</span><span class="p">]</span></div><div class='line' id='LC199'><br/></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">expected_structure</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;always Sanskrit&#39;</span><span class="p">,</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;always Tibetan&#39;</span><span class="p">,</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;Tibetan or Sanskrit&#39;</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">):</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">DCharsError</span><span class="p">(</span> <span class="n">context</span> <span class="o">=</span> <span class="s">&quot;DStringBOD.are_the_options_valid&quot;</span><span class="p">,</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">message</span> <span class="o">=</span> <span class="s">&quot;wrong options; unknown &#39;expected structure&#39; : &quot;</span><span class="o">+</span>\</div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">options</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC207'><br/></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_new_subfix</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC211'><span class="sd">                DStringBOD.get_new_subfix</span></div><div class='line' id='LC212'><br/></div><div class='line' id='LC213'><span class="sd">                Return a TriggerList associated to the alert__istructs_have_changed()</span></div><div class='line' id='LC214'><span class="sd">                function.</span></div><div class='line' id='LC215'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">TriggerList</span><span class="p">(</span> <span class="n">alert_function</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">alert__istructs_have_changed</span> <span class="p">)</span></div><div class='line' id='LC217'><br/></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_transliteration</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC221'><span class="sd">                DStringBOD.get_transliteration</span></div><div class='line' id='LC222'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Pylint can&#39;t know that &lt;self&gt; has a &#39;trans__get_transliteration_method&#39; member</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># created when &lt;self&gt; has been initialized by new_dstring() :</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># pylint: disable=E1101</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># -&gt; &quot;Instance of &#39;DStringBOD&#39; has no &#39;trans__get_transliteration_method&#39; member&quot;</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">DStringBOD</span><span class="o">.</span><span class="n">trans__get_transliteration</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">transliteration_method</span><span class="p">](</span><span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">res</span></div><div class='line' id='LC229'><br/></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">init_from_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">_str_src</span><span class="p">):</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC233'><span class="sd">                DStringBOD.init_from_str</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'><span class="sd">                Function called by __init__(), initialize &lt;self&gt; and return</span></div><div class='line' id='LC236'><span class="sd">                &lt;indexes_of_unrecognized_chars&gt;.</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'><span class="sd">                _str_src : str</span></div><div class='line' id='LC239'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">str_src</span> <span class="o">=</span> <span class="n">_str_src</span><span class="p">[:]</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">before</span><span class="p">,</span> <span class="n">after</span> <span class="ow">in</span> <span class="n">INIT_FROM_STR__SUBSTITUTIONS</span><span class="p">:</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">str_src</span> <span class="o">=</span> <span class="n">str_src</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">before</span><span class="p">,</span> <span class="n">after</span><span class="p">)</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># this is the function used to get the internal structure from a unicode string :</span></div><div class='line' id='LC245'><br/></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># empty istructs object :</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span> <span class="o">=</span> <span class="n">istruct</span><span class="o">.</span><span class="n">get_intstruct_from_str</span><span class="p">(</span><span class="n">_src</span> <span class="o">=</span> <span class="s">&quot;&quot;</span><span class="p">,</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span><span class="p">)</span></div><div class='line' id='LC249'><br/></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># We cut &lt;src&gt; into several substrings since the get_intstruct_from_str</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># function is VERY SLOW for long objects.</span></div><div class='line' id='LC252'><br/></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># We use str.split() in order to distinguish the common characters from the TSHEG character;</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we add a space after each substring except to the last one. The rules followed by</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># str.split() explain the strange use of &lt;last_substring&gt;.</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#       E.g :    &quot; a bc  e &quot;.split(&quot; &quot;)</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#             -&gt;[&#39;&#39;, &#39;a&#39;, &#39;bc&#39;, &#39;&#39;, &#39;e&#39;, &#39;&#39;]</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#       E.g :    &quot; a bc  e&quot;.split(&quot; &quot;)</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#             -&gt;[&#39;&#39;, &#39;a&#39;, &#39;bc&#39;, &#39;&#39;, &#39;e&#39;]</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">splitted_str</span> <span class="o">=</span> <span class="n">str_src</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">TSHEG_SYMBOL</span><span class="p">)</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index_substring</span><span class="p">,</span> <span class="n">substring</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">splitted_str</span><span class="p">):</span></div><div class='line' id='LC265'><br/></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">last_substring</span> <span class="o">=</span> <span class="p">(</span><span class="n">index_substring</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">splitted_str</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC267'><br/></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">substring</span> <span class="o">==</span> <span class="s">&#39;&#39;</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">last_substring</span><span class="p">:</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span> <span class="n">istruct</span><span class="o">.</span><span class="n">get_intstruct_from_str</span><span class="p">(</span> <span class="n">_src</span> <span class="o">=</span> <span class="n">TSHEG_SYMBOL</span><span class="p">,</span></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span><span class="p">))</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span> <span class="n">istruct</span><span class="o">.</span><span class="n">get_intstruct_from_str</span><span class="p">(</span> <span class="n">_src</span> <span class="o">=</span> <span class="n">substring</span><span class="p">,</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span> <span class="p">))</span></div><div class='line' id='LC274'><br/></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">last_substring</span><span class="p">:</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span> <span class="n">istruct</span><span class="o">.</span><span class="n">get_intstruct_from_str</span><span class="p">(</span> <span class="n">_src</span> <span class="o">=</span> <span class="n">TSHEG_SYMBOL</span><span class="p">,</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span> <span class="p">))</span></div><div class='line' id='LC278'><br/></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># by modifying all the InternalStructure objects (istruct.dstring__object = self) we</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># don&#39;t launch an alert since istruct.__setitem__ doesn&#39;t launch an alert.</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">set_the_dstring_object</span><span class="p">(</span> <span class="bp">self</span> <span class="p">)</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># let&#39;s modify the list of DCharacters :</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">alert__istructs_have_changed</span><span class="p">()</span></div><div class='line' id='LC284'><br/></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">init_from_transliteration</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">trans_src</span><span class="p">):</span></div><div class='line' id='LC287'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC288'><span class="sd">                DStringBOD.init_from_transliteration</span></div><div class='line' id='LC289'><br/></div><div class='line' id='LC290'><span class="sd">                trans_src     :       string</span></div><div class='line' id='LC291'><br/></div><div class='line' id='LC292'><span class="sd">                Return &lt;self&gt;</span></div><div class='line' id='LC293'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">alert_off</span><span class="p">()</span></div><div class='line' id='LC295'><br/></div><div class='line' id='LC296'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># this is the function used to get the internal structure from a transliterated string :</span></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Pylint can&#39;t know that &lt;self&gt; has a &#39;transliteration_method&#39; member</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># created when &lt;self&gt; has been initialized by new_dstring() :</span></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># pylint: disable=E1101</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># -&gt; &quot;Instance of &#39;DStringBOD&#39; has no &#39;transliteration_method&#39; member&quot;</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">get_intstruct</span> <span class="o">=</span> <span class="n">DStringBOD</span><span class="o">.</span><span class="n">trans__get_intstruct_from_trans_str</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">transliteration_method</span><span class="p">]</span></div><div class='line' id='LC303'><br/></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># We cut &lt;trans_src&gt; into several substrings since the get_intstruct_from_trans_str</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># function is VERY SLOW for long objects.</span></div><div class='line' id='LC306'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span> <span class="o">=</span> <span class="n">get_intstruct</span><span class="p">(</span> <span class="n">_src</span> <span class="o">=</span> <span class="s">&quot;&quot;</span><span class="p">,</span></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span> <span class="p">)</span></div><div class='line' id='LC308'><br/></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># We use str.split() in order to distinguish the common characters from the space character;</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we add a space after each substring except to the last one. The rules followed by</span></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># str.split() explain the strange use of &lt;last_substring&gt;.</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#       E.g :    &quot; a bc  e &quot;.split(&quot; &quot;)</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#             -&gt;[&#39;&#39;, &#39;a&#39;, &#39;bc&#39;, &#39;&#39;, &#39;e&#39;, &#39;&#39;]</span></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#       E.g :    &quot; a bc  e&quot;.split(&quot; &quot;)</span></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#             -&gt;[&#39;&#39;, &#39;a&#39;, &#39;bc&#39;, &#39;&#39;, &#39;e&#39;]</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#</span></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">splitted_str</span> <span class="o">=</span> <span class="n">trans_src</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">SPACE_SYMBOL</span><span class="p">)</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index_substring</span><span class="p">,</span> <span class="n">substring</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">splitted_str</span><span class="p">):</span></div><div class='line' id='LC321'><br/></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">last_substring</span> <span class="o">=</span> <span class="p">(</span><span class="n">index_substring</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">splitted_str</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC323'><br/></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">substring</span> <span class="o">==</span> <span class="s">&#39;&#39;</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">last_substring</span><span class="p">:</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span> <span class="n">get_intstruct</span><span class="p">(</span> <span class="n">_src</span> <span class="o">=</span> <span class="n">SPACE_SYMBOL</span><span class="p">,</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span> <span class="p">))</span></div><div class='line' id='LC327'><br/></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span> <span class="n">get_intstruct</span><span class="p">(</span> <span class="n">_src</span> <span class="o">=</span> <span class="n">substring</span><span class="p">,</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span> <span class="p">))</span></div><div class='line' id='LC331'><br/></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">last_substring</span><span class="p">:</span></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span> <span class="n">get_intstruct</span><span class="p">(</span> <span class="n">_src</span> <span class="o">=</span> <span class="n">SPACE_SYMBOL</span><span class="p">,</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span> <span class="p">))</span></div><div class='line' id='LC335'><br/></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the call to get_intstruct has set the alert on.</span></div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">alert_off</span><span class="p">()</span></div><div class='line' id='LC338'><br/></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># internalstructures -&gt; string</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">internalstructure</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="p">:</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">dchar</span> <span class="ow">in</span> <span class="n">internalstructure</span><span class="o">.</span><span class="n">get_the_corresponding_dchars</span><span class="p">(</span></div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dstring_object</span> <span class="o">=</span> <span class="bp">self</span><span class="p">,</span></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dcharactertype</span> <span class="o">=</span> <span class="n">DCharacterBOD</span><span class="p">):</span></div><div class='line' id='LC344'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">dchar</span> <span class="p">)</span></div><div class='line' id='LC345'><br/></div><div class='line' id='LC346'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">alert_on</span><span class="p">()</span></div><div class='line' id='LC347'><br/></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span></div><div class='line' id='LC349'><br/></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">is_identical_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">aliud</span><span class="p">):</span></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC353'><span class="sd">                DStringBOD.is_identical_to</span></div><div class='line' id='LC354'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC355'><br/></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># are the two list of DCharacterDOB objects identical ?</span></div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">aliud</span><span class="p">):</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC361'><br/></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">identical</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">dchar</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">dchar</span><span class="o">.</span><span class="n">is_identical_to</span><span class="p">(</span> <span class="n">aliud</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="p">):</span></div><div class='line' id='LC365'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">identical</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC366'><br/></div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">identical</span><span class="p">:</span></div><div class='line' id='LC368'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC369'><br/></div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># are the two istructs identical ?</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#.......................................................................</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">is_identical_to</span><span class="p">(</span> <span class="n">aliud</span><span class="o">.</span><span class="n">istructs</span> <span class="p">)</span></div><div class='line' id='LC374'><br/></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">load_the_buffers</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC378'><span class="sd">                DStringBOD.load_the_buffers</span></div><div class='line' id='LC379'><br/></div><div class='line' id='LC380'><span class="sd">                Return True if the buffers have been successfully loaded.</span></div><div class='line' id='LC381'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we load the buffer into BUFFER__FROM_STR :</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">bod_buffer</span><span class="o">.</span><span class="n">BUFFER__FROM_STR__FNAME</span></div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span> <span class="n">filename</span> <span class="p">):</span></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">DCharsError</span><span class="p">(</span> <span class="n">context</span> <span class="o">=</span> <span class="s">&quot; DStringBOD.__init__&quot;</span><span class="p">,</span></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">message</span> <span class="o">=</span> <span class="s">&quot;Missing file : &quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC387'><br/></div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="nb">open</span><span class="p">(</span> <span class="n">bod_buffer</span><span class="o">.</span><span class="n">BUFFER__FROM_STR__FNAME</span><span class="p">,</span> <span class="s">&#39;rb&#39;</span> <span class="p">)</span> <span class="k">as</span> <span class="n">bufferfile</span><span class="p">:</span></div><div class='line' id='LC389'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bod_buffer</span><span class="o">.</span><span class="n">BUFFER__FROM_STR</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span> <span class="n">bufferfile</span><span class="o">.</span><span class="n">read</span><span class="p">()</span> <span class="p">)</span></div><div class='line' id='LC390'><br/></div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># we load the buffer into EWTS_BUFFER__FROM_TRANS_STR :</span></div><div class='line' id='LC392'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">ewts_buffer</span><span class="o">.</span><span class="n">EWTS_BUFFER__FROM_TRANS_STR__FNAME</span><span class="p">)</span></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span> <span class="n">filename</span> <span class="p">):</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">DCharsError</span><span class="p">(</span> <span class="n">context</span> <span class="o">=</span> <span class="s">&quot; DStringBOD.__init__&quot;</span><span class="p">,</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">message</span> <span class="o">=</span> <span class="s">&quot;Missing file : &quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC396'><br/></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="nb">open</span><span class="p">(</span> <span class="n">ewts_buffer</span><span class="o">.</span><span class="n">EWTS_BUFFER__FROM_TRANS_STR__FNAME</span><span class="p">,</span> <span class="s">&#39;rb&#39;</span> <span class="p">)</span> <span class="k">as</span> <span class="n">bufferfile</span><span class="p">:</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ewts_buffer</span><span class="o">.</span><span class="n">EWTS_BUFFER__FROM_TRANS_STR</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span> <span class="n">bufferfile</span><span class="o">.</span><span class="n">read</span><span class="p">()</span> <span class="p">)</span></div><div class='line' id='LC399'><br/></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC401'><br/></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC403'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">sortingvalue</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC405'><span class="sd">                DStringBOD.sortingvalue</span></div><div class='line' id='LC406'><br/></div><div class='line' id='LC407'><span class="sd">                Return an SortingValue object</span></div><div class='line' id='LC408'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">sortingvalue</span><span class="p">()</span></div><div class='line' id='LC410'><br/></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#///////////////////////////////////////////////////////////////////////////</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">seems_to_be_a_sanskrit_string</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">strict_answer</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC414'><span class="sd">                DStringBOD.seems_to_be_a_sanskrit_string</span></div><div class='line' id='LC415'><br/></div><div class='line' id='LC416'><span class="sd">                Return a boolean.</span></div><div class='line' id='LC417'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">istructs</span><span class="o">.</span><span class="n">seems_to_be_a_sanskrit_string</span><span class="p">(</span><span class="n">strict_answer</span><span class="p">)</span></div><div class='line' id='LC419'><br/></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;">
            <button type="submit" class="button">Go</button>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="/about">About us</a></dd>
        <dd><a href="/blog">Blog</a></dd>
        <dd><a href="/contact">Contact &amp; support</a></dd>
        <dd><a href="https://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="https://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="https://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="https://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="https://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.13872s from fe17.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>
    <ul id="legal">
        <li><a href="/site/terms">Terms of Service</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/suizokukan/dchars/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
    <span id='server_response_time' data-time='0.13919' data-host='fe17'></span>
    
  </body>
</html>

