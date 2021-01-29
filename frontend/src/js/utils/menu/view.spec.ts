/* eslint-disable @typescript-eslint/no-non-null-assertion */
import View from './view'

declare const jsdom: {
  reconfigure: (config: { url: string }) => void
}

describe('Menu view', () => {
  let menu: HTMLElement,
    toggle: HTMLElement

  beforeEach(() => {
    document.body.innerHTML = `
<div>
  <a href="/">
    <img src="logo.png" />
  </a>
  </div>
    <button type="button" id="menu-toggle">
      Menú
    </button>
    <div id="site-menu">
      <ul>
        <li class="js-menu-item">
          <a href="/blog">Blog</a>
        </li>
        <li class="js-menu-item">
          <a href="/about">About</a>
        </li>
      </ul>
    </div>
  </div>
</div>`

    menu = document.getElementById('site-menu')!
    toggle = document.getElementById('menu-toggle')!
  })

  it('toggles menu visibility', () => {
    const view = new View(menu, toggle, 'hidden', 'active-link')

    view.toggleMenu()

    expect(menu.classList).toContain('hidden')

    view.toggleMenu()

    expect(menu.classList).not.toContain('hidden')
  })

  it('binds toggle click', () => {
    const handler = jest.fn()
    const view = new View(menu, toggle, 'hidden', 'active-link')
    view.bindToggleClick(handler)

    toggle.click()

    expect(handler).toHaveBeenCalled()
  })

  describe('Set active link', () => {
    it('detects current location', () => {
      jsdom.reconfigure({ url: 'http://example.com/blog/' })
      const link = menu.querySelector('a[href="/blog"]')!
      const view = new View(menu, toggle, 'hidden', 'active-link')

      view.setActiveLink()

      expect(link.classList).toContain('active-link')
    })

    it('detects nested location', () => {
      jsdom.reconfigure({ url: 'http://example.com/blog/post/' })
      const link = menu.querySelector('a[href="/blog"]')!
      const view = new View(menu, toggle, 'hidden', 'active-link')

      view.setActiveLink()

      expect(link.classList).toContain('active-link')
    })

    it('ignores links to new locations', () => {
      jsdom.reconfigure({ url: 'http://example.com/blog/' })
      const link = menu.querySelector('a[href="/about"]')!
      const view = new View(menu, toggle, 'hidden', 'active-link')

      view.setActiveLink()

      expect(link.classList).not.toContain('active-link')
    })
  })

  describe('User menu', () => {
    it('enables user menu', () => {
      document.body.innerHTML = `
<div>
  <a href="/">
    <img src="logo.png" />
  </a>
  </div>
    <button type="button" id="menu-toggle">
      Menú
    </button>
    <div id="site-menu">
      <div>
        <ul>
          <li class="js-menu-item">
            <a href="/blog">Blog</a>
          </li>
        </ul>
      </div>
      <button type="button" id="user-menu-toggle">
        User menu
      </button>
      <div id="user-menu">
        <ul>
          <li>
            <a href="/profile">profile</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>`

      menu = document.getElementById('site-menu')!
      toggle = document.getElementById('menu-toggle')!
      const userMenu = document.getElementById('user-menu')!
      const userMenuToggle = document.getElementById('user-menu-toggle')!
      const view = new View(menu, toggle, 'hidden', 'active-link')

      view.enableUserMenu()
      userMenuToggle.click()

      expect(userMenu.classList).toContain('hidden')

      userMenuToggle.click()

      expect(userMenu.classList).not.toContain('hidden')
    })

    it('handles missing user menu toggle', () => {
      document.body.innerHTML = `
<div>
  <a href="/">
    <img src="logo.png" />
  </a>
  </div>
    <button type="button" id="menu-toggle">
      Menú
    </button>
    <div id="site-menu">
      <div>
        <ul>
          <li class="js-menu-item">
            <a href="/blog">Blog</a>
          </li>
        </ul>
      </div>
      <div id="user-menu">
        <ul>
          <li>
            <a href="/profile">profile</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>`

      menu = document.getElementById('site-menu')!
      toggle = document.getElementById('menu-toggle')!
      const view = new View(menu, toggle, 'hidden', 'active-link')

      expect(view.enableUserMenu).not.toThrow()
    })

    it('handles missing user menu', () => {
      document.body.innerHTML = `
<div>
  <a href="/">
    <img src="logo.png" />
  </a>
  </div>
    <button type="button" id="menu-toggle">
      Menú
    </button>
    <div id="site-menu">
      <div>
        <ul>
          <li class="js-menu-item">
            <a href="/blog">Blog</a>
          </li>
        </ul>
      </div>
      <button type="button" id="user-menu-toggle">
        User menu
      </button>
    </div>
  </div>
</div>`

      menu = document.getElementById('site-menu')!
      toggle = document.getElementById('menu-toggle')!
      const userMenuToggle = document.getElementById('user-menu-toggle')!
      const view = new View(menu, toggle, 'hidden', 'active-link')

      view.enableUserMenu()

      expect(() => userMenuToggle.click()).not.toThrow()
    })

    it('accepts a custom class', () => {
      document.body.innerHTML = `
<div>
  <a href="/">
      <img src="logo.png" />
  </a>
  </div>
    <button type="button" id="menu-toggle">
      Menú
    </button>
    <div id="site-menu">
      <div>
        <ul>
          <li class="js-menu-item">
            <a href="/blog">Blog</a>
          </li>
        </ul>
      </div>
      <button type="button" id="user-menu-toggle">
        User menu
      </button>
      <div id="user-menu">
        <ul>
          <li>
            <a href="/profile">profile</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>`

      menu = document.getElementById('site-menu')!
      toggle = document.getElementById('menu-toggle')!
      const userMenu = document.getElementById('user-menu')!
      const userMenuToggle = document.getElementById('user-menu-toggle')!
      const view = new View(menu, toggle, 'hidden', 'active-link', 'custom-hide')

      view.enableUserMenu()
      userMenuToggle.click()

      expect(userMenu.classList).toContain('custom-hide')

      userMenuToggle.click()

      expect(userMenu.classList).not.toContain('custom-hide')
    })
  })
})
