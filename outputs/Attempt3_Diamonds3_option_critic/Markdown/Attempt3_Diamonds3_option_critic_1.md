
# Parameters

    Name :                      Attempt3_Diamonds3_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal6
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     25
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      35623051411 function calls (34508408780 primitive calls) in 258900.86 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.856 258900.856 {built-in method builtins.exec}
                      1    0.361    0.361 258900.856 258900.856 <string>:1(<module>)
                      1 4674.398 4674.398 258900.494 258900.494 optionCritic.py:195(option_critic_run)
               40050950 8731.430    0.000 104251.142    0.003 optionCritic.py:143(actor_loss_fn)
        1479575578/365037754 9691.047    0.000 101891.018    0.000 module.py:866(_call_impl)
              123837536  760.786    0.000 94090.165    0.001 optionCritic.py:70(get_state)
              123837536 2360.209    0.000 91041.194    0.001 container.py:117(forward)
                1602038   13.090    0.000 62755.846    0.039 tensor.py:195(backward)
                1602038   17.863    0.000 62742.506    0.039 __init__.py:68(backward)
                1602038 62683.449    0.039 62683.449    0.039 {method 'run_backward' of 'torch._C._EngineBase' objects}
              247675072  877.806    0.000 56120.865    0.000 conv.py:398(forward)
              247675072  486.658    0.000 54888.961    0.000 conv.py:390(_conv_forward)
              247675072 54402.303    0.000 54402.303    0.000 {built-in method conv2d}
                1602038   40.025    0.000 35945.421    0.022 optimizer.py:84(wrapper)
                1602038   25.900    0.000 35785.006    0.022 grad_mode.py:24(decorate_context)
                1602038  102.061    0.000 35715.728    0.022 rmsprop.py:56(step)
                1602038  148.984    0.000 35498.797    0.022 _functional.py:203(rmsprop)
               22428514 31929.799    0.001 31929.799    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               40050950 3471.495    0.000 20284.232    0.001 optionCritic.py:91(get_action)
              488875290 1445.984    0.000 20018.849    0.000 linear.py:93(forward)
              488875290  600.926    0.000 17974.554    0.000 functional.py:1737(linear)
              488875290 17250.495    0.000 17250.495    0.000 {built-in method torch._C._nn.linear}
               40050950 1217.593    0.000 14165.746    0.000 optionCritic.py:80(predict_option_termination)
               80101900 1247.141    0.000 7965.956    0.000 distribution.py:34(__init__)
              371512608  503.549    0.000 6958.509    0.000 activation.py:713(forward)
               40050950  582.235    0.000 6836.255    0.000 categorical.py:115(log_prob)
              371512608  470.937    0.000 6454.959    0.000 functional.py:1364(leaky_relu)
              371512608 5876.481    0.000 5876.481    0.000 {built-in method torch._C._nn.leaky_relu}
               40050950  747.197    0.000 5668.002    0.000 categorical.py:49(__init__)
              120887165  411.954    0.000 5625.275    0.000 optionCritic.py:77(get_Q)
               40050950  436.445    0.000 5608.457    0.000 bernoulli.py:34(__init__)
               80262103  404.990    0.000 4294.283    0.000 optionCritic.py:88(get_terminations)
               40050950 2316.239    0.000 3445.089    0.000 constraints.py:398(check)
                1602038   11.091    0.000 3384.765    0.002 game.py:42(step)
                1602038   20.138    0.000 3240.417    0.002 layers.py:827(step)
               40050950  471.311    0.000 2734.147    0.000 distribution.py:240(_validate_sample)
               22428514 2269.171    0.000 2269.171    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               40050950 2155.265    0.000 2155.265    0.000 constraints.py:364(check)
               40050950  424.547    0.000 2128.638    0.000 bernoulli.py:86(sample)
                 160203   32.437    0.000 2005.988    0.013 optionCritic.py:116(critic_loss_fn)
              123837536  192.556    0.000 2005.774    0.000 activation.py:101(forward)
               40050950  926.687    0.000 1874.005    0.000 categorical.py:123(entropy)
                1602038   68.557    0.000 1838.653    0.001 layers.py:17(step)
              123837536  176.876    0.000 1813.217    0.000 functional.py:1195(relu)
               40050950  120.602    0.000 1764.245    0.000 layer.py:106(move)
               40050950 1752.119    0.000 1752.119    0.000 constraints.py:249(check)
              120152850  225.393    0.000 1735.195    0.000 utils.py:106(__get__)
             1918244611 1680.670    0.000 1680.673    0.000 module.py:934(__getattr__)
              123837536 1606.895    0.000 1606.895    0.000 {built-in method relu}
              280356650 1548.860    0.000 1548.860    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               80101900  520.537    0.000 1514.713    0.000 functional.py:46(broadcast_tensors)
              123837536  171.160    0.000 1490.899    0.000 flatten.py:39(forward)
              120473256  186.559    0.000 1470.096    0.000 tensor.py:525(__rsub__)
                1602039  166.786    0.000 1373.515    0.001 layers.py:793(update)
             1497197996 1371.327    0.000 1371.327    0.000 {built-in method torch._C._get_tracing_state}
               40050950   72.747    0.000 1339.121    0.000 categorical.py:88(logits)
              123837536 1319.739    0.000 1319.739    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               40050950  349.055    0.000 1305.028    0.000 categorical.py:108(sample)
               40050950  273.539    0.000 1285.664    0.000 utils.py:11(broadcast_all)
               40050950   75.812    0.000 1266.374    0.000 utils.py:82(probs_to_logits)
              120473256 1256.529    0.000 1256.529    0.000 {built-in method rsub}
               80262103 1242.712    0.000 1242.712    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              120152850 1213.660    0.000 1213.660    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               17622418   49.781    0.000 1200.335    0.000 tensor.py:575(__iter__)
              120313053 1167.510    0.000 1167.510    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               17622418 1117.443    0.000 1117.443    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               40050950  231.926    0.000 1112.078    0.000 layers.py:844(check)
             6442889151  984.570    0.000  999.311    0.000 {built-in method builtins.len}
              120152850  996.151    0.000  996.151    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               80101900  854.144    0.000  854.144    0.000 {built-in method broadcast_tensors}
             6042139848  795.883    0.000  795.883    0.000 {method 'values' of 'collections.OrderedDict' objects}
               40050950  142.674    0.000  789.688    0.000 utils.py:77(clamp_probs)
               40050950  785.011    0.000  785.011    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               40050950  696.521    0.000  696.521    0.000 {built-in method bernoulli}
                1602038   74.838    0.000  652.400    0.000 replaybuffer.py:34(save_option_critic)
               40050950  647.014    0.000  647.014    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               40050950  633.161    0.000  633.161    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               40464859  585.585    0.000  585.585    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              120633459  585.559    0.000  585.559    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               40050950  517.269    0.000  517.269    0.000 {built-in method clamp}
               80101900  502.098    0.000  502.098    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1602038   86.092    0.000  497.545    0.000 optimizer.py:189(zero_grad)
              240626106  485.100    0.000  485.100    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               22428514  447.259    0.000  447.259    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               40050950  106.006    0.000  438.130    0.000 layers.py:838(isFree)
               12816312  250.831    0.000  416.764    0.000 layer.py:175(NoRock_update)
               40050950  407.934    0.000  407.934    0.000 {built-in method all}
               40050950  400.874    0.000  400.874    0.000 {built-in method log}
              527413036  246.229    0.000  389.251    0.000 {built-in method builtins.isinstance}
               22428514  380.540    0.000  380.540    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 160203  303.906    0.002  378.281    0.002 replaybuffer.py:42(sample_option_critic)
               40050950  374.748    0.000  374.748    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               10092841  358.232    0.000  358.232    0.000 {built-in method tensor}
              120152875  104.812    0.000  356.571    0.000 {built-in method builtins.all}
              123837550  333.584    0.000  333.584    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              308986971  274.997    0.000  332.124    0.000 layer.py:103(isFree)
                 413933    9.123    0.000  329.617    0.001 layers.py:849(restart)
               40050950  328.617    0.000  328.617    0.000 {built-in method multinomial}
               22428514  323.044    0.000  323.044    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              120569987  320.061    0.000  320.061    0.000 {method 'item' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 239, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607850: <Attempt3_Diamonds3_option_critic_1> in cluster <dcc> Exited

Job <Attempt3_Diamonds3_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
Job was executed on host(s) <n-62-21-92>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:25 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:25 2021
Terminated at Thu May  6 13:26:33 2021
Results reported at Thu May  6 13:26:33 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258069.69 sec.
    Max Memory :                                 901 MB
    Average Memory :                             885.10 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15483.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258907 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

