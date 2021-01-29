import View from './view'

class Controller {
  timerId: ReturnType<typeof setTimeout> | null = null

  constructor (private readonly view: View) {}

  init (): void {
    this.view.bindNotificationClick(this.view.closeNotification)
    this.timerId = this.view.setCloseTimer(10)
  }
}

export default Controller
