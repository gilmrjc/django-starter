class View {
  constructor (private readonly element: HTMLElement) {}

  bindNotificationClick (handler: (this: View) => void): void {
    this.element.addEventListener('click', handler)
  }

  readonly closeNotification = (): void => {
    this.element.remove()
  }

  readonly setCloseTimer = (seconds: number): ReturnType<typeof setTimeout> => setTimeout(
    this.closeNotification, seconds * 1000
  )
}

export default View
