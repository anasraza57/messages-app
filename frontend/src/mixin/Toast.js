import {
  createToaster
} from "@meforma/vue-toaster";

export const toast = {
  toaster: createToaster({
    position: "top-right",
    max: 3,
  }),

  SuccessToast(message) {
    this.toaster.success(message)
  },
  ErrorToast(message) {
    this.toaster.error(message)
  }
}