# // Copyright 2016 The Chromium Authors. All rights reserved.
# // Use of this source code is governed by a BSD-style license that can be
# // found in the LICENSE file.

# // This file was generated at (2016-11-18 07:04:40.019257) by running:
# //
# ../../chrome/test/chromedriver/embed_js_in_cpp.py --directory gen/chrome/test/chromedriver/chrome
# ../../chrome/test/chromedriver/js/add_cookie.js
# ../../chrome/test/chromedriver/js/call_function.js
# ../../chrome/test/chromedriver/js/execute_async_script.js
# ../../chrome/test/chromedriver/js/focus.js
# ../../chrome/test/chromedriver/js/get_element_region.js
# ../../chrome/test/chromedriver/js/is_option_element_toggleable.js

#include "chrome/test/chromedriver/chrome/js.h"

kFocusScript = '''
    function() { // Copyright (c) 2013 The Chromium Authors. All rights reserved.
    // Use of this source code is governed by a BSD-style license that can be
    // found in the LICENSE file.

    function focus(element) {
      // Focus the target element in order to send keys to it.
      // First, the currently active element is blurred, if it is different from
      // the target element. We do not want to blur an element unnecessarily,
      // because this may cause us to lose the current cursor position in the
      // element.
      // Secondly, we focus the target element.
      // Thirdly, if the target element is newly focused and is a text input, we
      // set the cursor position at the end.
      // Fourthly, we check if the new active element is the target element. If not,
      // we throw an error.
      // Additional notes:
      //   - |document.activeElement| is the currently focused element, or body if
      //     no element is focused
      //   - Even if |document.hasFocus()| returns true and the active element is
      //     the body, sometimes we still need to focus the body element for send
      //     keys to work. Not sure why
      //   - You cannot focus a descendant of a content editable node
      //   - V8 throws a TypeError when calling setSelectionRange for a non-text
      //     input, which still have setSelectionRange defined. For chrome 29+, V8
      //     throws a DOMException with code InvalidStateError.
      var doc = element.ownerDocument || element;
      var prevActiveElement = doc.activeElement;
      if (element != prevActiveElement && prevActiveElement)
        prevActiveElement.blur();
      element.focus();
      if (element != prevActiveElement && element.value &&
          element.value.length && element.setSelectionRange) {
        try {
          element.setSelectionRange(element.value.length, element.value.length);
        } catch (error) {
          if (!(error instanceof TypeError) && !(error instanceof DOMException &&
              error.code == DOMException.INVALID_STATE_ERR))
            throw error;
        }
      }

      var activeElement = doc.activeElement;
      // If the element is in a shadow DOM, then as far as the document is
      // concerned, the shadow host is the active element. We need to go through the
      // tree of shadow DOMs to check that the element we gave focus to is now
      // active.
      if (element != activeElement) {
        var shadowRoot = activeElement.shadowRoot;
        while (shadowRoot) {
          var activeElement = shadowRoot.activeElement;
          if (element == activeElement) {
            // the shadow DOM's active element is our requested element. We're good.
            break;
          }
          // The shadow DOM's active element isn't our requested element, check to
          // see if there's a nested shadow DOM.
          shadowRoot = activeElement.shadowRoot;
        }
      }
      if (element != activeElement)
        throw new Error('cannot focus element');
    }
    ; return focus.apply(null, arguments) }

    '''
kGetElementRegionScript = '''
    function() { // Copyright (c) 2013 The Chromium Authors. All rights reserved.
    // Use of this source code is governed by a BSD-style license that can be
    // found in the LICENSE file.

    function getElementRegion(element) {
      // Check that node type is element.
      if (element.nodeType != 1)
        throw new Error(element + ' is not an element');

      // We try 2 methods to determine element region. Try the first client rect,
      // and then the bounding client rect.
      // SVG is one case that doesn't have a first client rect.
      var clientRects = element.getClientRects();

      // Element area of a map has same first ClientRect and BoundingClientRect
      // after blink roll at chromium commit position 290738 which includes blink
      // revision 180610. Thus handle area as a special case.
      if (clientRects.length == 0 || element.tagName.toLowerCase() == 'area') {
        var box = element.getBoundingClientRect();
        if (element.tagName.toLowerCase() == 'area') {
          var coords = element.coords.split(',');
          if (element.shape.toLowerCase() == 'rect') {
            if (coords.length != 4)
              throw new Error('failed to detect the region of the area');
            var leftX = Number(coords[0]);
            var topY = Number(coords[1]);
            var rightX = Number(coords[2]);
            var bottomY = Number(coords[3]);
            return {
                'left': leftX,
                'top': topY,
                'width': rightX - leftX,
                'height': bottomY - topY
            };
          } else if (element.shape.toLowerCase() == 'circle') {
            if (coords.length != 3)
              throw new Error('failed to detect the region of the area');
            var centerX = Number(coords[0]);
            var centerY = Number(coords[1]);
            var radius = Number(coords[2]);
            return {
                'left': Math.max(0, centerX - radius),
                'top': Math.max(0, centerY - radius),
                'width': radius * 2,
                'height': radius * 2
            };
          } else if (element.shape.toLowerCase() == 'poly') {
            if (coords.length < 2)
              throw new Error('failed to detect the region of the area');
            var minX = Number(coords[0]);
            var minY = Number(coords[1]);
            var maxX = minX;
            var maxY = minY;
            for (i = 2; i < coords.length; i += 2) {
              var x = Number(coords[i]);
              var y = Number(coords[i + 1]);
              minX = Math.min(minX, x);
              minY = Math.min(minY, y);
              maxX = Math.max(maxX, x);
              maxY = Math.max(maxY, y);
            }
            return {
                'left': minX,
                'top': minY,
                'width': maxX - minX,
                'height': maxY - minY
            };
          } else {
            throw new Error('shape=' + element.shape + ' is not supported');
          }
        }
        return {
            'left': 0,
            'top': 0,
            'width': box.width,
            'height': box.height
        };
      } else {
        var box = element.getBoundingClientRect();
        var clientRect = clientRects[0];
        for (var i = 0; i < clientRects.length; i++) {
          if (clientRects[i].height != 0 && clientRects[i].width != 0) {
            clientRect = clientRects[i];
            break;
          }
        }
        return {
            'left': clientRect.left - box.left,
            'top': clientRect.top - box.top,
            'width': clientRect.right - clientRect.left,
            'height': clientRect.bottom - clientRect.top
        };
      }
    }
    ; return getElementRegion.apply(null, arguments) }

    '''
kIsOptionElementToggleableScript = '''
    function() { // Copyright (c) 2013 The Chromium Authors. All rights reserved.
    // Use of this source code is governed by a BSD-style license that can be
    // found in the LICENSE file.

    function isOptionElementToggleable(option) {
      if (option.tagName.toLowerCase() != 'option')
        throw new Error('element is not an option');
      for (var parent = option.parentElement;
           parent;
           parent = parent.parentElement) {
        if (parent.tagName.toLowerCase() == 'select') {
          return parent.multiple;
        }
      }
      throw new Error('option element is not in a select');
    }
    ; return isOptionElementToggleable.apply(null, arguments) }

    '''
kExecuteAsyncScriptScript = '''
    function() { // Copyright (c) 2013 The Chromium Authors. All rights reserved.
    // Use of this source code is governed by a BSD-style license that can be
    // found in the LICENSE file.

    /**
     * Enum for WebDriver status codes.
     * @enum {number}
     */
    var StatusCode = {
      OK: 0,
      UNKNOWN_ERROR: 13,
      JAVASCRIPT_ERROR: 17,
      SCRIPT_TIMEOUT: 28,
    };

    /**
     * Dictionary key for asynchronous script info.
     * @const
     */
    var ASYNC_INFO_KEY = '$chrome_asyncScriptInfo';

    /**
    * Return the information of asynchronous script execution.
    *
    * @return {Object<?>} Information of asynchronous script execution.
    */
    function getAsyncScriptInfo() {
      if (!(ASYNC_INFO_KEY in document))
        document[ASYNC_INFO_KEY] = {'id': 0};
      return document[ASYNC_INFO_KEY];
    }

    /**
    * Execute the given script and save its asynchronous result.
    *
    * If script1 finishes after script2 is executed, then script1's result will be
    * discarded while script2's will be saved.
    *
    * @param {string} script The asynchronous script to be executed. The script
    *     should be a proper function body. It will be wrapped in a function and
    *     invoked with the given arguments and, as the final argument, a callback
    *     function to invoke to report the asynchronous result.
    * @param {!Array<*>} args Arguments to be passed to the script.
    * @param {boolean} isUserSupplied Whether the script is supplied by the user.
    *     If not, UnknownError will be used instead of JavaScriptError if an
    *     exception occurs during the script, and an additional error callback will
    *     be supplied to the script.
    * @param {?number} opt_timeoutMillis The timeout, in milliseconds, to use.
    *     If the timeout is exceeded and the callback has not been invoked, a error
    *     result will be saved and future invocation of the callback will be
    *     ignored.
    */
    function executeAsyncScript(script, args, isUserSupplied, opt_timeoutMillis) {
      var info = getAsyncScriptInfo();
      info.id++;
      delete info.result;
      var id = info.id;

      function report(status, value) {
        if (id != info.id)
          return;
        info.id++;
        info.result = {status: status, value: value};
      }
      function reportValue(value) {
        report(StatusCode.OK, value);
      }
      function reportScriptError(error) {
        var code = isUserSupplied ? StatusCode.JAVASCRIPT_ERROR :
                                    (error.code || StatusCode.UNKNOWN_ERROR);
        var message = error.message;
        if (error.stack) {
          message += \"\\nJavaScript stack:\\n\" + error.stack;
        }
        report(code, message);
      }
      args.push(reportValue);
      if (!isUserSupplied)
        args.push(reportScriptError);

      try {
        new Function(script).apply(null, args);
      } catch (error) {
        reportScriptError(error);
        return;
      }

      if (typeof(opt_timeoutMillis) != 'undefined') {
        window.setTimeout(function() {
          var code = isUserSupplied ? StatusCode.SCRIPT_TIMEOUT :
                                      StatusCode.UNKNOWN_ERROR;
          var errorMsg = 'result was not received in ' + opt_timeoutMillis / 1000 +
                         ' seconds';
          report(code, errorMsg);
        }, opt_timeoutMillis);
      }
    }
    ; return executeAsyncScript.apply(null, arguments) }

    '''
kCallFunctionScript = '''
    function() { // Copyright (c) 2012 The Chromium Authors. All rights reserved.
    // Use of this source code is governed by a BSD-style license that can be
    // found in the LICENSE file.

    /**
     * Enum for WebDriver status codes.
     * @enum {number}
     */
    var StatusCode = {
      STALE_ELEMENT_REFERENCE: 10,
      UNKNOWN_ERROR: 13,
    };

    /**
     * Enum for node types.
     * @enum {number}
     */
    var NodeType = {
      ELEMENT: 1,
      DOCUMENT: 9,
    };

    /**
     * Dictionary key to use for holding an element ID.
     * @const
     * @type {string}
     */
    var ELEMENT_KEY = 'ELEMENT';

    /**
     * True if shadow dom is enabled.
     * @const
     * @type {boolean}
     */
    var SHADOW_DOM_ENABLED = typeof ShadowRoot === 'function';

    /**
     * A cache which maps IDs <-> cached objects for the purpose of identifying
     * a script object remotely.
     * @constructor
     */
    function Cache() {
      this.cache_ = {};
      this.nextId_ = 1;
      this.idPrefix_ = Math.random().toString();
    }

    Cache.prototype = {

      /**
       * Stores a given item in the cache and returns a unique ID.
       *
       * @param {!Object} item The item to store in the cache.
       * @return {number} The ID for the cached item.
       */
      storeItem: function(item) {
        for (var i in this.cache_) {
          if (item == this.cache_[i])
            return i;
        }
        var id = this.idPrefix_  + '-' + this.nextId_;
        this.cache_[id] = item;
        this.nextId_++;
        return id;
      },

      /**
       * Retrieves the cached object for the given ID.
       *
       * @param {number} id The ID for the cached item to retrieve.
       * @return {!Object} The retrieved item.
       */
      retrieveItem: function(id) {
        var item = this.cache_[id];
        if (item)
          return item;
        var error = new Error('not in cache');
        error.code = StatusCode.STALE_ELEMENT_REFERENCE;
        error.message = 'element is not attached to the page document';
        throw error;
      },

      /**
       * Clears stale items from the cache.
       */
      clearStale: function() {
        for (var id in this.cache_) {
          var node = this.cache_[id];
          if (!this.isNodeReachable_(node))
            delete this.cache_[id];
        }
      },

      /**
        * @private
        * @param {!Node} node The node to check.
        * @return {boolean} If the nodes is reachable.
        */
      isNodeReachable_: function(node) {
        var nodeRoot = getNodeRootThroughAnyShadows(node);
        return (nodeRoot == document);
      }
    };

    /**
     * Returns the root element of the node.  Found by traversing parentNodes until
     * a node with no parent is found.  This node is considered the root.
     * @param {!Node} node The node to find the root element for.
     * @return {!Node} The root node.
     */
    function getNodeRoot(node) {
      while (node.parentNode) {
        node = node.parentNode;
      }
      return node;
    }

    /**
     * Returns the root element of the node, jumping up through shadow roots if
     * any are found.
     */
    function getNodeRootThroughAnyShadows(node) {
      var root = getNodeRoot(node);
      while (SHADOW_DOM_ENABLED && root instanceof ShadowRoot) {
        root = getNodeRoot(root.host);
      }
      return root;
    }

    /**
     * Returns the global object cache for the page.
     * @param {Document=} opt_doc The document whose cache to retrieve. Defaults to
     *     the current document.
     * @return {!Cache} The page's object cache.
     */
    function getPageCache(opt_doc) {
      var doc = opt_doc || document;
      var key = '$cdc_asdjflasutopfhvcZLmcfl_';
      if (!(key in doc))
        doc[key] = new Cache();
      return doc[key];
    }

    /**
     * Wraps the given value to be transmitted remotely by converting
     * appropriate objects to cached object IDs.
     *
     * @param {*} value The value to wrap.
     * @return {*} The wrapped value.
     */
    function wrap(value) {
      // As of crrev.com/1316933002, typeof() for some elements will return
      // 'function', not 'object'. So we need to check for both non-null objects, as
      // well Elements that also happen to be callable functions (e.g. <embed> and
      // <object> elements). Note that we can not use |value instanceof Object| here
      // since this does not work with frames/iframes, for example
      // frames[0].document.body instanceof Object == false even though
      // typeof(frames[0].document.body) == 'object'.
      if ((typeof(value) == 'object' && value != null) ||
          (typeof(value) == 'function' && value instanceof Element)) {
        var nodeType = value['nodeType'];
        if (nodeType == NodeType.ELEMENT || nodeType == NodeType.DOCUMENT
            || (SHADOW_DOM_ENABLED && value instanceof ShadowRoot)) {
          var wrapped = {};
          var root = getNodeRootThroughAnyShadows(value);
          wrapped[ELEMENT_KEY] = getPageCache(root).storeItem(value);
          return wrapped;
        }

        var obj = (typeof(value.length) == 'number') ? [] : {};
        for (var prop in value)
          obj[prop] = wrap(value[prop]);
        return obj;
      }
      return value;
    }

    /**
     * Unwraps the given value by converting from object IDs to the cached
     * objects.
     *
     * @param {*} value The value to unwrap.
     * @param {Cache} cache The cache to retrieve wrapped elements from.
     * @return {*} The unwrapped value.
     */
    function unwrap(value, cache) {
      if (typeof(value) == 'object' && value != null) {
        if (ELEMENT_KEY in value)
          return cache.retrieveItem(value[ELEMENT_KEY]);

        var obj = (typeof(value.length) == 'number') ? [] : {};
        for (var prop in value)
          obj[prop] = unwrap(value[prop], cache);
        return obj;
      }
      return value;
    }

    /**
     * Calls a given function and returns its value.
     *
     * The inputs to and outputs of the function will be unwrapped and wrapped
     * respectively, unless otherwise specified. This wrapping involves converting
     * between cached object reference IDs and actual JS objects. The cache will
     * automatically be pruned each call to remove stale references.
     *
     * @param  {Array<string>} shadowHostIds The host ids of the nested shadow
     *     DOMs the function should be executed in the context of.
     * @param {function(...[*]) : *} func The function to invoke.
     * @param {!Array<*>} args The array of arguments to supply to the function,
     *     which will be unwrapped before invoking the function.
     * @param {boolean=} opt_unwrappedReturn Whether the function's return value
     *     should be left unwrapped.
     * @return {*} An object containing a status and value property, where status
     *     is a WebDriver status code and value is the wrapped value. If an
     *     unwrapped return was specified, this will be the function's pure return
     *     value.
     */
    function callFunction(shadowHostIds, func, args, opt_unwrappedReturn) {
      var cache = getPageCache();
      cache.clearStale();
      if (shadowHostIds && SHADOW_DOM_ENABLED) {
        for (var i = 0; i < shadowHostIds.length; i++) {
          var host = cache.retrieveItem(shadowHostIds[i]);
          // TODO(zachconrad): Use the olderShadowRoot API when available to check
          // all of the shadow roots.
          cache = getPageCache(host.webkitShadowRoot);
          cache.clearStale();
        }
      }

      if (opt_unwrappedReturn)
        return func.apply(null, unwrap(args, cache));

      var status = 0;
      try {
        var returnValue = wrap(func.apply(null, unwrap(args, cache)));
      } catch (error) {
        status = error.code || StatusCode.UNKNOWN_ERROR;
        var returnValue = error.message;
      }
      return {
          status: status,
          value: returnValue
      }
    }
    ; return callFunction.apply(null, arguments) }

    '''
kAddCookieScript = '''
    function() { // Copyright (c) 2013 The Chromium Authors. All rights reserved.
    // Use of this source code is governed by a BSD-style license that can be
    // found in the LICENSE file.

    /**
    * Test whether the given domain is valid for a cookie.
    *
    * @param {string} domain Domain for a cookie.
    * @return {boolean} True if the domain is valid, otherwise false.
    */
    function isDomainValid(domain) {
      var dummyCookie = 'ChromeDriverwjers908fljsdf37459fsdfgdfwru=';

      document.cookie = dummyCookie + '; domain=' + domain;
      if (document.cookie.indexOf(dummyCookie) != -1) {
        // Expire the dummy cookie if it is added successfully.
        document.cookie = dummyCookie + '; Max-Age=0; domain=' + domain;
        return true;
      }
      return false;
    }

    /**
    * Add the given cookie to the current web page.
    *
    * If path is not specified, default to '/'.
    * If domain is not specified, default to document.domain, otherwise remove its
    * port number.
    *
    * Validate name, value, domain and path of the cookie in the same way as the
    * method CanonicalCookie::Create in src/net/cookies/canonical_cookie.cc. Besides
    * the following requirements, name, value, domain and path of the cookie should
    * not start or end with ' ' or '\\t', and should not contain '\\n', '\\r', or '\\0'.
    * <ul>
    * <li>name: no ';' or '='
    * <li>value: no ';'
    * <li>path: starts with '/', no ';'
    * </ul>
    *
    * @param {!Object} cookie An object representing a Cookie JSON Object as
    *     specified in https://code.google.com/p/selenium/wiki/JsonWireProtocol.
    */
    function addCookie(cookie) {
      function isNameInvalid(value) {
        return /(^[ \\t])|([;=\\n\\r\\0])|([ \\t]$)/.test(value);
      }
      function isValueInvalid(value) {
        return /(^[ \\t])|([;\\n\\r\\0])|([ \\t]$)/.test(value);
      }
      function isPathInvalid(path) {
        return path[0] != '/' || /([;\\n\\r\\0])|([ \\t]$)/.test(path);
      }

      var name = cookie['name'];
      if (!name || isNameInvalid(name))
        throw new Error('name of cookie is missing or invalid:\"' + name + '\"');

      var value = cookie['value'] || '';
      if (isValueInvalid(value))
        throw new Error('value of cookie is invalid:\"' + value + '\"');

      var domain = cookie['domain'];
      // Remove the port number from domain.
      if (domain) {
        var domain_parts = domain.split(':');
        if (domain_parts.length > 2)
          throw new Error('domain of cookie has too many colons');
        else if (domain_parts.length == 2)
          domain = domain_parts[0];
      }
      // Validate domain.
      if (domain && (isValueInvalid(domain) || !isDomainValid(domain))) {
        var error = new Error();
        error.code = 24;  // Error code for InvalidCookieDomain.
        error.message = 'invalid domain:\"' + domain + '\"';
        throw error;
      }

      var path = cookie['path'];
      if (path && isPathInvalid(path))
        throw new Error('path of cookie is invalid:\"' + path + '\"');

      var newCookie = name + '=' + value;
      newCookie += '; path=' + (path || '/');
      if (domain)
        newCookie += '; domain=' + domain;
      if (cookie['expiry']) {
        var expiredDate = new Date(cookie['expiry'] * 1000);
        newCookie += '; expires=' + expiredDate.toUTCString();
      }
      if (cookie['secure'])
        newCookie += '; secure';

      document.cookie = newCookie;
    }
    ; return addCookie.apply(null, arguments) }
    '''
