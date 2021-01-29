import Controller from './controller'
import View from './view'

describe('Notification controller', () => {
  let view: {
      bindNotificationClick: jest.Mock
      closeNotification: jest.Mock
      setCloseTimer: jest.Mock
    },
    controller: Controller

  beforeEach(() => {
    view = {
      bindNotificationClick: jest.fn(),
      closeNotification: jest.fn(),
      setCloseTimer: jest.fn()
    }
    controller = new Controller(view as unknown as View)
  })

  describe('Init', () => {
    it('binds toggle button', () => {
      controller.init()

      expect(view.bindNotificationClick).toHaveBeenCalledWith(view.closeNotification)
    })

    it('sets close timer for notification', () => {
      controller.init()

      expect(view.setCloseTimer).toHaveBeenCalled()
    })
  })
})
