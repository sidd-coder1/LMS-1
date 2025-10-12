import React from 'react';
import { Box, Card, CardContent, Typography, Divider, Stack } from '@mui/material';

const Settings: React.FC = () => {
  return (
    <Box>
      <Typography variant="h4" component="h1" gutterBottom sx={{ fontWeight: 'bold', mb: 3 }}>
        Settings
      </Typography>

      <Stack spacing={2}>
        <Card>
          <CardContent>
            <Typography variant="h6" sx={{ fontWeight: 600, mb: 1 }}>
              Account
            </Typography>
            <Divider sx={{ mb: 2 }} />
            <Typography variant="body2" color="text.secondary">
              Manage your account details here.
            </Typography>
          </CardContent>
        </Card>
      </Stack>
    </Box>
  );
};

export default Settings;
