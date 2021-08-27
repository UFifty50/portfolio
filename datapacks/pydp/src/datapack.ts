/**
 * 
 */

import { MCFunction, NBT, tellraw, Data, Variable, _, item, raw } from 'sandstone'

function getdata() {
  const chestplate = Data('entity', '@s').select('Inventory', [{Slot: NBT.byte(102)}]);
  const itemCount = Variable(-1);
  const inv = Data('entity', '@s');
  for (let i = 0; i < 36; i++) {
    var slot = inv.select('Inventory', [{ Slot: NBT.byte(i) }]);
    itemCount.set(slot.select('Count'));

    _.if(itemCount.notEqualTo(0), () => {
      tellraw('@a', 'Slot was not empty!');
    })

      .else(() => {
        replaceitem('@s', "armor.chest").with("minecraft:golden_chestplate", 1)
        item.replace.entity('@s', "armor.chest").with("minecraft:golden_chestplate", 1)
        tellraw('@a', 'Slot was empty.')
    })
  }
}

MCFunction('check_for_empty_slots', () => {
  getdata()
}, {
  runOnLoad: false,
})

MCFunction('load', () => {
  tellraw("@a", { text: ' Loaded!', color: 'gold', bold: true })
}, {
  runOnLoad: true,
})