import createMenu from './menu'
import Controller from './menu/controller'

describe('createMenu', () => {
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
      </ul>
    </div>
  </div>
</div>`
  })

  it('returns undefined when the menu element is not found', () => {
    const menu = createMenu('bad-selector', 'menu-toggle', 'hidden', 'active-link')

    expect(menu).toBeUndefined()
  })

  it('returns undefined when the toggle element is not found', () => {
    const menu = createMenu('site-menu', 'bad-selector', 'hidden', 'active-link')

    expect(menu).toBeUndefined()
  })

  it('creates the menu controller', () => {
    const menu = createMenu('site-menu', 'menu-toggle', 'hidden', 'active-link')

    expect(menu).toBeInstanceOf(Controller)
  })
})
