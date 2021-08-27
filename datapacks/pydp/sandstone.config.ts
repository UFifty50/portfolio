import type { SandstoneConfig } from 'sandstone'

export default {
  name: 'pydp',
  description: [ 'A ', { text: 'Sandstone', color: 'gold' }, ' data pack.' ],
  formatVersion: 6,
  namespace: 'a',
  packUid: '_xC1DBE2',
  saveOptions: { path: 'C:\\Users\\Jonathan\\AppData\\Roaming\\.minecraft\\saves\\datapack test world\\datapacks\\' },
  onConflict: {
    default: 'warn',
  },
} as SandstoneConfig
