import View from './view'

class Controller {
  constructor (private readonly view: View) {}

  init (): void {
    this.view.setActiveLink()
    this.view.bindToggleClick(this.view.toggleMenu)
    this.view.enableUserMenu()
  }

  setActiveLink (): void {
    this.view.setActiveLink()
  }
}

export default Controller
