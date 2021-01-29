import Controller from './controller'
import View from './view'

describe('Menu controller', () => {
  let view: {
      bindToggleClick: jest.Mock
      enableUserMenu: jest.Mock
      setActiveLink: jest.Mock
      toggleMenu: jest.Mock
    },
    controller: Controller

  beforeEach(() => {
    view = {
      bindToggleClick: jest.fn(),
      enableUserMenu: jest.fn(),
      setActiveLink: jest.fn(),
      toggleMenu: jest.fn()
    }
    controller = new Controller(view as unknown as View)
  })

  it('sets active link', () => {
    controller.setActiveLink()

    expect(view.setActiveLink).toHaveBeenCalled()
  })

  describe('Init', () => {
    it('sets active link', () => {
      controller.init()

      expect(view.setActiveLink).toHaveBeenCalled()
    })

    it('binds toggle button', () => {
      controller.init()

      expect(view.bindToggleClick).toHaveBeenCalledWith(view.toggleMenu)
    })

    it('enables user menu', () => {
      controller.init()

      expect(view.enableUserMenu).toHaveBeenCalled()
    })
  })
})
