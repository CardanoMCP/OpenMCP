import { OpenMCPCardanoClient } from '../src/client';

const client = new OpenMCPCardanoClient();
console.log(client.health()); 