import View from './view'

jest.useFakeTimers()

describe('Menu view', () => {
  let notification: HTMLElement

  beforeEach(() => {
    document.body.innerHTML = `
<div class="js-notification">
  Successs
</div>`

    notification = document.getElementsByClassName('js-notification')[0] as HTMLDivElement
  })

  it('binds notification click', () => {
    const handler = jest.fn()
    const view = new View(notification)
    view.bindNotificationClick(handler)

    notification.click()

    expect(handler).toHaveBeenCalled()
  })

  it('removes the notification', () => {
    const view = new View(notification)

    view.closeNotification()

    const notifications = document.getElementsByClassName('js-notification')
    expect(notifications.length).toBe(0)
  })

  it('sets notification close timmer', () => {
    const view = new View(notification)

    view.setCloseTimer(1)

    expect(setTimeout).toHaveBeenCalledWith(view.closeNotification, 1000)
  })
})
