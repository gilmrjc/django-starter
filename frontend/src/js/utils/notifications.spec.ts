import createNotification from './notifications'
import Controller from './notifications/controller'

describe('createNotification', () => {
  let notificationElement: HTMLElement

  beforeEach(() => {
    document.body.innerHTML = `
<div class="js-notification">
  Successs
</div>`

    notificationElement = document.getElementsByClassName('js-notification')[0] as HTMLDivElement
  })

  it('creates the notification controller', () => {
    const notification = createNotification(notificationElement)

    expect(notification).toBeInstanceOf(Controller)
  })
})
