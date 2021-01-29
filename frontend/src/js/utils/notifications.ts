import Controller from './notifications/controller'
import View from './notifications/view'

function createNofitication (element: HTMLElement): Controller {
  return new Controller(new View(element))
}

export default createNofitication
