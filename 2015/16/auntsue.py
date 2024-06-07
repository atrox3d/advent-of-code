from dataclasses import dataclass, fields, asdict
import re

@dataclass
class AuntSue:
    id: int
    children: int = None
    cats: int = None
    samoyeds: int = None
    pomeranians: int = None
    akitas: int = None
    vizslas: int = None
    goldfish: int = None
    trees: int = None
    cars: int = None
    perfumes: int = None

    @classmethod
    def from_string(cls, string):
        aunt_pattern = r'^Sue (?P<id>\d+): (?P<properties>.+)'
        props_pattern = r'(?P<thing>\w+): (?P<qty>\d+)'

        for line in string.splitlines():
            result = re.match(aunt_pattern, line)
            aunt_id, props = result.groupdict().values()
            aunt = cls(aunt_id)
            # aunts[aunt_id] = {}
            for prop in props.split(', '):
                thing, qty = re.match(props_pattern, prop).groupdict().values()
                setattr(aunt, thing, int(qty))

    def __eq__(self, value: object) -> bool:
        for name, this, other in zip(asdict(self), asdict(self).values(), asdict(value).values()):
            # print(name, this, other)
            if name == 'id':
                continue
            if this != other and this is not None:
                # print(self.id, f'{name}: {this} != {other}')
                break
        else:
            return True
        return False

class AuntSue2(AuntSue):
    '''
    the cats and trees readings indicates that there are greater than that many 
    
    the pomeranians and goldfish readings indicate that there are fewer than that many 
    '''
    def __eq__(self, value: object) -> bool:

        #   loop through each attribute 
        for name, this, tape in zip(asdict(self), asdict(self).values(), asdict(value).values()):
            
            if name == 'id':            # ignore id
                continue


            if this is None:            # everything else can be None
                continue

            # the cats and trees readings indicates that there are greater than that many 
            if name in ['cats', 'trees']:
                if this >= tape:
                    # print(f'{self.id}: cats, trees >= tape')
                    continue
                else:
                    break

            # the pomeranians and goldfish readings indicate that there are fewer than that many 
            if name in ['pomeranians', 'goldfish']:
                if this <= tape:
                    # print(f'{self.id}: pomeridians, goldfish <= tape')
                    continue
                else:
                    break
            else:
                if this != tape:        # if not it must match
                    break

        else:
            print(self.id, f'{self}')   # found
            return True
        
        # print(self.id, f'{self}')     # not found
        return False
    


if __name__ == '__main__':
    a1 = AuntSue(1, cats=2)
    a2 = AuntSue(2, cats=2)
    print(a1==a2)

