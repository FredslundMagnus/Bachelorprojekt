
# Parameters

    Name :                      SuperLevel2_teleport-1
    Main :                      teleport
    Level :                     Levels.SuperLevel2
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      91045493268 function calls (90820442389 primitive calls) in 86109.48 seconds

##    Ordered by: cumulative time
   List reduced from 483 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.484 86109.484 {built-in method builtins.exec}
                      1    1.493    1.493 86109.483 86109.483 <string>:1(<module>)
                      1  187.745  187.745 86107.990 86107.990 main.py:45(teleport)
                4040068   17.752    0.000 31034.602    0.008 game.py:41(step)
                8080136   28.707    0.000 30387.342    0.004 agent.py:29(learn)
                4040068   22.162    0.000 29907.334    0.007 layers.py:718(step)
                8080136  714.618    0.000 26069.628    0.003 learner.py:42(Qlearn)
                4040068  374.835    0.000 22054.931    0.005 layers.py:17(step)
              404006800 1406.905    0.000 21642.955    0.000 layer.py:98(move)
                4040068  141.178    0.000 18267.669    0.005 agent.py:54(_learn)
              404006800 2329.653    0.000 15280.375    0.000 layers.py:735(check)
                4040068  115.423    0.000 12072.293    0.003 agent.py:117(_learn)
        253230849/28180981 1082.822    0.000 11764.473    0.000 module.py:715(_call_impl)
                8080136   50.315    0.000 11208.126    0.001 grad_mode.py:23(decorate_context)
                8080136  285.885    0.000 11064.412    0.001 adam.py:55(step)
               20100845   54.717    0.000 11023.704    0.001 network.py:27(forward)
               20100845  273.740    0.000 10845.237    0.001 container.py:115(forward)
                8080136 2039.955    0.000 9546.276    0.001 functional.py:53(adam)
                4040069  597.604    0.000 7801.536    0.002 layers.py:684(update)
                7980641  188.336    0.000 7136.449    0.001 agent.py:49(__call__)
                4040068 2485.900    0.001 5992.976    0.001 agent.py:88(interveen)
                8080136   53.019    0.000 5927.249    0.001 tensor.py:181(backward)
                8080136   31.958    0.000 5874.230    0.001 __init__.py:68(backward)
                8080136 5614.187    0.001 5614.187    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4040068 3090.107    0.001 5082.928    0.001 replaybuffer.py:22(sample_data)
                4040068 2499.147    0.001 4783.726    0.001 agent.py:67(modify)
                4040068 2401.739    0.001 4703.161    0.001 replaybuffer.py:28(teleporter_save_data)
              404006800  841.882    0.000 4055.499    0.000 layers.py:729(isFree)
               40201690   72.562    0.000 3890.451    0.000 conv.py:422(forward)
               40201690   83.875    0.000 3790.112    0.000 conv.py:414(_conv_forward)
               40201690 3691.521    0.000 3691.521    0.000 {built-in method conv2d}
               52222399  127.889    0.000 3541.168    0.000 linear.py:92(forward)
              404006800 2450.724    0.000 3427.156    0.000 layers.py:471(check)
               52222399  223.057    0.000 3359.057    0.000 functional.py:1669(linear)
             3786877294 2500.038    0.000 3213.617    0.000 layer.py:95(isFree)
               44440759 1850.690    0.000 3111.215    0.000 layer.py:151(update)
            10911022573 2016.990    0.000 2943.409    0.000 enum.py:646(__hash__)
             1130049632  760.375    0.000 2850.688    0.000 {built-in method builtins.any}
               52222399 2402.631    0.000 2402.631    0.000 {built-in method addmm}
              509048622 1468.490    0.000 2312.987    0.000 tensor.py:933(grad)
                4040068   58.124    0.000 2276.142    0.001 agent.py:112(__call__)
                8080136  199.520    0.000 2236.888    0.000 optimizer.py:167(zero_grad)
              404006800 1504.706    0.000 2149.111    0.000 layers.py:77(check)
               12020709   97.023    0.000 2137.354    0.000 agent.py:59(modify_board)
               32221049 2085.420    0.000 2085.420    0.000 {built-in method cat}
              145442448 1994.456    0.000 1994.456    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              404006800 1141.866    0.000 1928.339    0.000 layers.py:286(check)
              116159971 1888.961    0.000 1888.961    0.000 {built-in method clone}
              404006800 1030.772    0.000 1835.673    0.000 layers.py:246(check)
              145442448 1691.449    0.000 1691.449    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4040068   75.574    0.000 1684.948    0.000 replaybuffer.py:18(stacker)
             4792701396 1361.391    0.000 1659.718    0.000 layers.py:700(<genexpr>)
               72323244   67.024    0.000 1644.516    0.000 activation.py:713(forward)
               17303244 1609.108    0.000 1609.108    0.000 {built-in method tensor}
               72323244  108.800    0.000 1577.492    0.000 functional.py:1292(leaky_relu)
               72323244 1458.744    0.000 1458.744    0.000 {built-in method torch._C._nn.leaky_relu}
               12020709 1334.432    0.000 1334.432    0.000 {built-in method torch._C._nn.one_hot}
                8080136   11.498    0.000 1259.919    0.000 game.py:37(board)
            12424787929 1243.487    0.000 1243.487    0.000 layer.py:91(positions)
               28283640  165.194    0.000 1171.870    0.000 tensor.py:21(wrapped)
              662275177  391.398    0.000 1153.078    0.000 overrides.py:1070(has_torch_function)
               72721224 1087.229    0.000 1087.229    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4040068  625.203    0.000 1050.507    0.000 collector.py:46(collect)
                4615117   56.628    0.000 1020.921    0.000 layers.py:740(restart)
               72721224  993.715    0.000  993.715    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
            10911052060  926.425    0.000  926.425    0.000 {built-in method builtins.hash}
               72721224  906.811    0.000  906.811    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              432290540  172.692    0.000  815.569    0.000 {built-in method builtins.all}
               72721224  809.525    0.000  809.525    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              404006800  517.379    0.000  777.188    0.000 layers.py:313(check)
                7980641  266.235    0.000  756.998    0.000 exploration.py:53(softmaxer)
             1325895741  746.003    0.000  746.003    0.000 layer.py:146(elements)
              404006800  480.265    0.000  745.475    0.000 layers.py:273(check)
             1616028400  439.926    0.000  673.724    0.000 layers.py:690(<genexpr>)
               72721224  636.725    0.000  636.725    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              404006800  414.071    0.000  601.718    0.000 layers.py:62(check)
              128180680  598.651    0.000  598.651    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              404006800  376.366    0.000  574.531    0.000 layers.py:48(check)
        5937890604/5937890602  442.545    0.000  572.021    0.000 {built-in method builtins.len}
              392399708  203.081    0.000  531.514    0.000 random.py:285(choice)
                4615117   27.192    0.000  508.633    0.000 level.py:8(__init__)
                8080136   12.506    0.000  502.186    0.000 loss.py:445(forward)
               20200340  494.119    0.000  494.119    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                8080136   47.519    0.000  489.680    0.000 functional.py:2637(mse_loss)
               52222399  475.825    0.000  475.825    0.000 {method 't' of 'torch._C._TensorBase' objects}
              404006800  320.226    0.000  464.531    0.000 layers.py:23(check)
               50766287   60.465    0.000  438.832    0.000 layer.py:69(restart)
             1405055595  343.846    0.000  424.788    0.000 overrides.py:1083(<genexpr>)
               24240408  421.940    0.000  421.940    0.000 {built-in method sum}
              594453779  291.995    0.000  421.241    0.000 random.py:250(_randbelow_with_getrandbits)
             4889042604  407.903    0.000  407.903    0.000 {method 'random' of '_random.Random' objects}
             3014077887  386.941    0.000  386.941    0.000 layer.py:203(isBlocking)
              619196822  268.218    0.000  361.213    0.000 layer.py:130(add)
                8080136  308.285    0.000  308.285    0.000 {built-in method torch._C._nn.mse_loss}
               40201690   31.491    0.000  303.293    0.000 flatten.py:39(forward)
                4040068  110.341    0.000  300.175    0.000 random.py:315(sample)
              337671520  187.622    0.000  288.927    0.000 layer.py:126(remove)
                4041664  276.813    0.000  276.813    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                8081338  275.732    0.000  275.732    0.000 {built-in method max}
               40201690  271.802    0.000  271.802    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550912: <SuperLevel2_teleport_1> in cluster <dcc> Done

Job <SuperLevel2_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:50 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 24 17:57:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 17:57:30 2021
Terminated at Sun Apr 25 17:52:45 2021
Results reported at Sun Apr 25 17:52:45 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
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

    CPU time :                                   85897.80 sec.
    Max Memory :                                 2679 MB
    Average Memory :                             2676.22 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13705.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86135 sec.
    Turnaround time :                            437455 sec.

The output (if any) is above this job summary.

