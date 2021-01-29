import Controller from './menu/controller'
import View from './menu/view'

function createMenu (
  menuId: string,
  toggleId: string,
  hiddenClass: string,
  activeLinkClass: string,
  userMenuHiddenClass?: string
): Controller | undefined {
  const menu = document.getElementById(menuId)
  const toggle = document.getElementById(toggleId)

  if (menu === null || toggle === null) {
    return undefined
  }

  return new Controller(new View(menu, toggle, hiddenClass, activeLinkClass, userMenuHiddenClass))
}

export default createMenu
