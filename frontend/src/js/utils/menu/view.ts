class View {
  private readonly userMenuHiddenClass: string

  constructor (
    private readonly menu: HTMLElement,
    private readonly toggle: HTMLElement,
    private readonly hiddenClass: string,
    private readonly activeLinkClass: string,
    userMenuHiddenClass? : string
  ) {
    this.userMenuHiddenClass = userMenuHiddenClass ?? hiddenClass
  }

  bindToggleClick (handler: EventHandlerNonNull): void {
    this.toggle.addEventListener('click', handler)
  }

  readonly enableUserMenu = (): void => {
    const userMenuToggle = this.menu.querySelector('#user-menu-toggle')
    const userMenu = this.menu.querySelector('#user-menu')

    if (userMenuToggle === null || userMenu === null) {
      return
    }

    userMenuToggle.addEventListener('click', () => {
      userMenu.classList.toggle(this.userMenuHiddenClass)
    })
  }

  setActiveLink (): void {
    const menuItems: NodeListOf<HTMLAnchorElement> = this.menu.querySelectorAll('.js-menu-item a')

    menuItems.forEach((item) => {
      const subdirection = document.location.href.includes(item.href)

      if (subdirection) {
        item.classList.add(this.activeLinkClass)
      }
    })
  }

  readonly toggleMenu: (this: View) => void = (): void => {
    this.menu.classList.toggle(this.hiddenClass)
  }
}

export default View
