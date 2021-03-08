
# Parameters

    Name :                      maze_size_15_low_rest_chance-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     15
    Height :                    15
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      11080727780 function calls (10963545509 primitive calls) in 35694.37 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.479 35710.479 {built-in method builtins.exec}
                      1    0.796    0.796 35710.479 35710.479 <string>:1(<module>)
                      1   97.535   97.535 35709.683 35709.683 main.py:10(teleport)
                4187130   14.611    0.000 12052.954    0.003 agent.py:26(learn)
                2093565  280.664    0.000 11379.915    0.005 collector.py:36(collect)
               10467825 10245.525    0.001 11070.510    0.001 {built-in method builtins.sum}
                4187130  318.412    0.000 10306.357    0.002 learner.py:42(Qlearn)
                2093565   78.795    0.000 7206.953    0.003 agent.py:50(_learn)
        131776932/14645904  539.250    0.000 4999.951    0.000 module.py:866(_call_impl)
                2093565   66.412    0.000 4820.548    0.002 agent.py:101(_learn)
               10458774   31.331    0.000 4665.857    0.000 network.py:24(forward)
               10458774  147.427    0.000 4569.925    0.000 container.py:117(forward)
                4187130   38.194    0.000 4298.328    0.001 optimizer.py:84(wrapper)
                4187130   17.769    0.000 4124.757    0.001 grad_mode.py:24(decorate_context)
                4187130  115.325    0.000 4066.229    0.001 adam.py:55(step)
                4187130  845.513    0.000 3816.468    0.001 _functional.py:53(adam)
                2093565    8.479    0.000 3448.415    0.002 game.py:21(step)
                4178079  105.920    0.000 3097.976    0.001 agent.py:45(__call__)
                2093565   10.104    0.000 2970.343    0.001 layers.py:212(step)
                4187130   18.561    0.000 2568.651    0.001 tensor.py:195(backward)
                4187130   16.412    0.000 2549.398    0.001 __init__.py:68(backward)
                2093565 1003.980    0.000 2538.885    0.001 agent.py:77(interveen)
                4187130 2439.069    0.001 2439.069    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2093565 1086.738    0.001 1973.073    0.001 replaybuffer.py:27(teleporter_save_data)
               20917548   48.898    0.000 1686.030    0.000 conv.py:398(forward)
               20917548   27.001    0.000 1617.381    0.000 conv.py:390(_conv_forward)
               20917548 1590.380    0.000 1590.380    0.000 {built-in method conv2d}
                2093565  861.327    0.000 1510.248    0.001 agent.py:59(modify)
                2093565  720.467    0.000 1482.387    0.001 replaybuffer.py:23(sample_data)
                2093565  135.129    0.000 1476.981    0.001 layers.py:17(step)
                2093566  179.768    0.000 1468.750    0.001 layers.py:192(update)
              209356500  144.961    0.000 1321.036    0.000 layer.py:66(move)
               27189192   61.200    0.000 1302.539    0.000 linear.py:93(forward)
               27189192   23.448    0.000 1216.170    0.000 functional.py:1737(linear)
               27189192 1187.242    0.000 1187.242    0.000 {built-in method torch._C._nn.linear}
                2093565   32.619    0.000  961.317    0.000 agent.py:96(__call__)
              209356500   87.198    0.000  928.975    0.000 layers.py:223(isFree)
                6271644   40.437    0.000  924.972    0.000 agent.py:54(modify_board)
               12562224   23.586    0.000  855.721    0.000 tensor.py:575(__iter__)
              298502888  787.148    0.000  841.777    0.000 layer.py:63(isFree)
               12562224  809.239    0.000  809.239    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               16739469  771.586    0.000  771.586    0.000 {built-in method cat}
               75368340  768.650    0.000  768.650    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               59763915  753.872    0.000  753.872    0.000 {built-in method clone}
               37647966   39.645    0.000  735.589    0.000 activation.py:713(forward)
               37647966   33.046    0.000  695.943    0.000 functional.py:1364(leaky_relu)
               75368340  687.476    0.000  687.476    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8864895  676.503    0.000  676.503    0.000 {built-in method tensor}
               37647966  655.954    0.000  655.954    0.000 {built-in method torch._C._nn.leaky_relu}
                2093565   39.935    0.000  618.798    0.000 replaybuffer.py:19(stacker)
                4187130   99.923    0.000  614.367    0.000 optimizer.py:189(zero_grad)
                6271644  597.555    0.000  597.555    0.000 {built-in method torch._C._nn.one_hot}
                4187130    4.784    0.000  531.526    0.000 game.py:17(board)
              209356600   53.841    0.000  511.213    0.000 {built-in method builtins.all}
              628156863  137.373    0.000  479.905    0.000 layers.py:197(<genexpr>)
                 505760    5.180    0.000  459.331    0.001 layers.py:233(restart)
               37684170  428.708    0.000  428.708    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 505760    1.216    0.000  375.523    0.001 levels.py:8(__init__)
                 505760    2.555    0.000  374.307    0.001 level.py:8(__init__)
               37684170  369.488    0.000  369.488    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 505760   77.392    0.000  366.411    0.001 levels.py:11(generate)
               37684170  354.144    0.000  354.144    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               37684170  351.213    0.000  351.213    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              209356600  215.668    0.000  326.167    0.000 layers.py:65(isDone)
                4178079  118.261    0.000  323.401    0.000 exploration.py:53(softmaxer)
               37684170  280.136    0.000  280.136    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6280698  108.368    0.000  265.457    0.000 layer.py:90(update)
              263789244  182.429    0.000  226.147    0.000 tensor.py:906(grad)
               66035559  208.918    0.000  208.918    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4187130    6.332    0.000  207.589    0.000 loss.py:527(forward)
                4187130   16.303    0.000  201.257    0.000 functional.py:2898(mse_loss)
                 505760  100.476    0.000  194.081    0.000 levels.py:76(RFS)
              209356500  145.378    0.000  188.513    0.000 layers.py:229(check)
                2599325   54.489    0.000  144.130    0.000 random.py:315(sample)
                4187130  132.639    0.000  132.639    0.000 {built-in method torch._C._nn.mse_loss}
               20917548   14.170    0.000  124.184    0.000 flatten.py:39(forward)
                4187756  117.915    0.000  117.915    0.000 {built-in method max}
        619621799/619621797   80.768    0.000  115.800    0.000 {built-in method builtins.len}
                6280695    9.334    0.000  115.623    0.000 tensor.py:525(__rsub__)
              233021699  113.504    0.000  113.504    0.000 layer.py:85(elements)
               20917548  110.014    0.000  110.014    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              144339156  105.753    0.000  105.753    0.000 {built-in method torch._C._get_tracing_state}
                6280695  104.695    0.000  104.695    0.000 {built-in method rsub}
                4178079  102.131    0.000  102.131    0.000 {built-in method multinomial}
                2093565    8.075    0.000   97.609    0.000 exploration.py:47(epsilonGreedy)
             1091774591   94.010    0.000   94.010    0.000 layer.py:59(positions)
                4187130   93.167    0.000   93.167    0.000 {built-in method gather}
                4187130   16.882    0.000   90.148    0.000 __init__.py:28(_make_grads)
                8374260   18.914    0.000   88.670    0.000 profiler.py:615(__enter__)
                1517280    7.160    0.000   78.020    0.000 layer.py:40(restart)
              130535090   52.747    0.000   76.797    0.000 random.py:250(_randbelow_with_getrandbits)
                2093566   74.961    0.000   74.961    0.000 {built-in method nonzero}
                8374260   12.234    0.000   73.691    0.000 profiler.py:607(__init__)
              258921083   49.856    0.000   71.872    0.000 enum.py:646(__hash__)
                4187130   69.971    0.000   69.971    0.000 {built-in method ones_like}
                8374260   69.756    0.000   69.756    0.000 {built-in method torch._ops.profiler._record_function_enter}
                4670242   67.608    0.000   67.608    0.000 {method 'long' of 'torch._C._TensorBase' objects}
                4178496    4.984    0.000   62.467    0.000 functional.py:1553(softmax)
              106682582   62.203    0.000   62.209    0.000 module.py:934(__getattr__)
                8374262   61.462    0.000   61.462    0.000 {built-in method zeros}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9393246: <maze_size_15_low_rest_chance_0> in cluster <dcc> Done

Job <maze_size_15_low_rest_chance_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 02:11:20 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 02:11:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 02:11:21 2021
Terminated at Mon Mar  8 12:06:50 2021
Results reported at Mon Mar  8 12:06:50 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35591.75 sec.
    Max Memory :                                 5292 MB
    Average Memory :                             3911.08 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2900.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35771 sec.
    Turnaround time :                            35730 sec.

The output (if any) is above this job summary.

